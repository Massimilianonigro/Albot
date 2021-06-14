from os import stat
from albot_backend.state import State
import json
import random as rand
from albot_backend.question_handler import QuestionHandler
from albot_backend.inform_handler import InformHandler
from albot_backend.enum_encoder import get_dict


RESOURCES_PATH = "./resources"

""" [summary] StateMachine class decides the utterances and changes of state given from the chatbot, given user's state and input.
"""


class StateMachine:
    def __init__(self):
        self.utterances = json.load(open(RESOURCES_PATH + "/utterances.json", "r"))
        self.behaviour = get_dict(RESOURCES_PATH + "/trial.json")
        self.question_handler = QuestionHandler()
        self.inform_handler = InformHandler()

    def _get_state(self, current_state):
        for state in self.behaviour["state_machine"]:
            if state["state"] == current_state:
                return state
        return None

    def input_function(self, intent, current_state, pending_question):
        print(
            "In state_machine input_function: "
            + str(current_state)
            + ", intent recognized is: "
            + str(intent["intent"]["name"])
        )
        state = self._get_state(current_state)
        if state != None:
            return self._intent_response(state, intent, pending_question)
        else:
            raise Exception("State not found")

    def _intent_response(self, state, intent, pending_question):
        intent_name = intent["intent"]["name"]
        utterance = self._get_utterance(state, intent_name)
        utterance_array = []
        new_pending_question = pending_question
        next_state = state["state"]
        bot_response = {}
        # Case 1: The intent is recognized in the state's utterances
        if utterance != None:
            return self._response_to_intent(
                utterance, new_pending_question, next_state, utterance_array
            )
        # Case 2: The intent is a click not present in the state's utterances and the state has reaction to a click
        if self._has_click_reaction(state) and self._is_intent_click(intent_name):
            print("entering in case 2 with intent: " + intent_name)
            return self._click_reaction(
                state, intent_name, new_pending_question, next_state, utterance_array
            )
        # Case 3: The child has a question pending, intent could be answering to the question
        if pending_question != None:
            does_answer_advance_state = self.question_handler.does_answer_advance_state(
                pending_question
            )
            does_answer_reverse_state = self.question_handler.does_answer_reverse_state(
                pending_question, intent_name
            )
            t = ()
            t = self._check_question_answer(pending_question, intent_name)
            # If response is None than the child may be asking a question
            if t != None:
                new_pending_question, response = t
                print("entering in case 3 with intent: " + intent_name)
                next_state = (
                    self.get_next_state(next_state)
                    if does_answer_advance_state
                    else next_state
                )
                next_state = (
                    self.get_previous_state(next_state)
                    if does_answer_reverse_state
                    else next_state
                )
                print(response)
                utterance_array = utterance_array + self._get_utterances(response)
                bot_response = self._create_message(utterance_array)
                return new_pending_question, next_state, bot_response
        # Case 4: Intent could be asking for an explanation
        question_explanation = self._general_questions(intent)
        if question_explanation != None:
            utterance_array = utterance_array + self._get_utterances(
                [question_explanation]
            )
            bot_response = self._create_message(utterance_array)
            return new_pending_question, next_state, bot_response
        # Case 5: Intent not understood, fallback
        if (
            intent_name == "nlu_fallback" or not self._is_intent_click(intent_name)
        ) and intent_name != "wait_ended":
            utterance_array = utterance_array + self._get_utterances(["fallback"])
            bot_response = self._create_message(utterance_array)
        return new_pending_question, next_state, bot_response

    def _response_to_intent(
        self, utterance, new_pending_question, next_state, utterance_array
    ):
        change_phase = ""
        if "question_type" in utterance.keys():
            new_pending_question, question = self._get_chatbot_question(
                utterance["question_type"]
            )
            utterance_array = utterance_array + [self._create_utterance(text=question)]
        elif "child_answer" in utterance.keys():
            utterance_array = utterance_array + self._get_utterances(
                [self.question_handler.get_explanation_by_id(new_pending_question)]
            )
            print("utterance_array after moreinfo click is " + str(utterance_array))
        if "next_state" in utterance.keys():
            next_state = utterance["next_state"]
        if "new_pending_question" in utterance.keys():
            new_pending_question = utterance["new_pending_question"]
            print("Setting pending question in response_to_intent(state machine)")
        if "to_send_back" in utterance.keys():
            utterance_array = utterance_array + self._get_utterances(
                utterance["to_send_back"]
            )
        if "change_phase" in utterance.keys():
            change_phase = utterance["change_phase"]
        response = self._create_message(utterance_array, change_phase)
        print("Next state will be: " + str(next_state))
        return new_pending_question, next_state, response

    def _is_intent_click(self, intent):
        return intent[0:7] == "clicked"

    def _create_utterance(self, text="", ui_effect=""):
        return {"text": text, "ui_effect": ui_effect}

    def _create_message(self, utterance_array, change_phase=""):
        response = {"messages": utterance_array, "change_phase": change_phase}
        return response

    def _click_reaction(
        self, state, intent_name, new_pending_question, next_state, utterance_array
    ):
        clicked_object_id = str(intent_name[8:])
        utterance_array = utterance_array + self._get_utterances(
            state["click_object_reaction"]["to_send_back"]
        )
        print(self._get_utterances(state["click_object_reaction"]["to_send_back"]))
        if self._has_display(state):
            utterance_array = utterance_array + [
                self._create_utterance(text="display_" + clicked_object_id)
            ]
        if "new_pending_question" in state["click_object_reaction"]:
            if state["click_object_reaction"]["new_pending_question"] == "clicked":
                # Function that understands the question id from the question name
                question_id = self.question_handler.get_first_id_from_question_name(
                    "searching_" + clicked_object_id
                )
                if question_id != None:
                    new_pending_question = question_id
            else:
                new_pending_question = state["click_object_reaction"][
                    "new_pending_question"
                ]
        if "next_state" in state["click_object_reaction"]:
            next_state = state["click_object_reaction"]["next_state"]
        response = self._create_message(utterance_array)
        return new_pending_question, next_state, response

    def _check_question_answer(self, pending_question, intent):
        is_answer_correct = self.question_handler.verify_answer(
            pending_question, intent
        )
        print("is_answer_correct is " + str(is_answer_correct))
        if is_answer_correct != 2:
            return self.question_handler.get_response(
                pending_question, is_answer_correct
            )
        else:
            return None

    def _get_utterance(self, state, intent):
        for utterance in state["utterances"]:
            if utterance["intent"] == intent:
                return utterance
        return None

    def _get_chatbot_question(self, question_type):
        new_pending_question = self.question_handler.get_random_question(question_type)
        question = self.question_handler.get_question_by_id(new_pending_question)
        return new_pending_question, question

    def _is_key_in_dict(self, key, dict):
        if key in dict.keys():
            return True
        else:
            return False

    def _has_click_reaction(self, state):
        return self._is_key_in_dict("click_object_reaction", state)

    def _has_display(self, state):
        return self._is_key_in_dict("display", state)

    # Answer general questions of the user that can be done over all the interaction, takes in an intent and gives back a string
    def _general_questions(self, intent):
        if intent["intent"]["name"][0:6] == "inform":
            return self.inform_handler.grant_information(intent)
        else:
            return None

    # Determines if at the beginning of the state there is a branch between chatbot or child question
    def is_branch(self, state_enum):
        state = self._get_state(state_enum)
        return self._is_key_in_dict("optional", state)

    def is_waiting(self, state_enum):
        state = self._get_state(state_enum)
        return self._is_key_in_dict("waiting", state)

    def get_waiting_time(self):
        return self.behaviour["waiting_time"]

    def get_question_multiplier(self):
        return self.behaviour["question_multiplier"]

    def is_cycle(self, state_enum):
        state = self._get_state(state_enum)
        return self._is_key_in_dict("cycle", state)

    def get_next_state(self, state_enum):
        if self.is_cycle(state_enum):
            return state_enum
        else:
            return State(state_enum.value + 1)

    def get_previous_state(self, state_enum):
        if self.is_cycle(state_enum):
            return state_enum
        else:
            return State(state_enum.value - 1)

    def _get_utterances(self, utterance_names):
        utterances = []
        for name in utterance_names:
            if name != None:
                utterance = rand.choice(self.utterances[name])
                if not (utterance["ui_effect"] == "" and utterance["text"] == ""):
                    utterances.append(utterance)
        return utterances
