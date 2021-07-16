from os import sendfile
from albot_backend.state import State
from albot_backend.state_machine import StateMachine
import json
import random
import asyncio
import requests
import time

LOGS_PATH = "./logs"

""" [summary] DialogueManager is the link between the NLU Module and the State Machine, fully controls user's experience 
"""


class DialogueManager:

    users = {}

    def __init__(self, handler):
        self.state_machine = StateMachine()
        self.handler = handler

    async def add_user(self, user_session_id):
        self.users[user_session_id] = {
            "current_state": State.GREETING,
            "is_coro_ended": None,
            "pending_question": None,
            "question_probability": 1,
            "conversation": [],
            "user_code": "",
            "start_time": "",
            "end_time": "",
        }
        # The moment the user is added the chatbot greets him and introduces him to the lesson
        intent = self._create_intent("connected")
        await self.chatbot_sends_message(intent, user_session_id)

    def del_user(self, user_session_id):
        del self.users[user_session_id]

    def _append_log_entry(self, subject, text, user_id):
        entry = {
            "subject": subject,
            "text": text,
            "time": time.strftime("%H:%M:%S"),
        }
        self.users[user_id]["conversation"].append(entry)

    # msg structure is {"text": text
    #                  "highlighted": objectId
    #                   }
    def chatbot_receives_message(self, msg, user_id):
        # First the messsage has to be deserialized
        msg = json.loads(msg)
        # Control if the text field is empty
        if msg["type"] == "text":
            # The message is now forwarded to the Rasa NLU and an intent comes back
            print("text received " + str(msg["content"]))
            self._append_log_entry(self.users[user_id]["name"], msg["content"], user_id)
            intent = self._nlu_parse(msg["content"])
            # Request to do http requests to rasa container
        elif msg["type"] == "click":
            # If the length of the text is empty the user acted on the interface selecting an object
            obj = msg["content"].replace(" ", "")
            obj = obj.lower()
            self._append_log_entry(
                self.users[user_id]["name"], "clicked_" + obj, user_id
            )
            print("object clicked " + obj)
            intent = self._create_intent("clicked_" + obj)
        elif msg["type"] == "name":
            self.users[user_id]["name"] = msg["content"]
            intent = self._create_intent("given_name")
        elif msg["type"] == "guessed":
            intent = self._create_intent("guessed_" + str(msg["content"]))
            self._append_log_entry(
                self.users[user_id]["name"], "guessed_" + str(msg["content"]), user_id
            )
        elif msg["type"] == "name_request":
            return json.dumps(
                {
                    "messages": [
                        {"text": self.users[user_id]["name"], "ui_effect": "hidden"}
                    ],
                    "change_phase": "",
                }
            )
        elif msg["type"] == "user_code":
            self.users[user_id]["user_code"] = msg["content"]
            self.users[user_id]["start_time"] = time.strftime("%d-%m-%Y-%H:%M:%S")
            return
        elif msg["type"] == "end_conversation":
            self.users[user_id]["end_time"] = time.strftime("%d-%m-%Y-%H:%M:%S")
            self._write_log(user_id)
            return
        elif msg["type"] == "selection_complete":
            intent = self._create_intent("selection_complete")
            self._append_log_entry(
                self.users[user_id]["name"],
                "selection_complete" + str(self.users[user_id]["current_state"]),
                user_id,
            )
        elif msg["type"] == "selection_complete_2":
            intent = self._create_intent("selection_complete_2")
            self._append_log_entry(
                self.users[user_id]["name"],
                "selection_complete" + str(self.users[user_id]["current_state"]),
                user_id,
            )
        elif msg["type"] == "click_tripetto":
            intent = self._create_intent("click_tripetto")
        elif msg["type"] == "click_tripetto_2":
            intent = self._create_intent("click_tripetto_2")
        # Now that i have the intent calculated i can generate a response and move the child on the state machine
        utterance = self.generate_utterance(intent, user_id)
        utterance_after_replace = self.replace_name(utterance, user_id)
        self._log_bot_messages(utterance_after_replace, user_id)
        return utterance_after_replace

    def _write_log(self, user_id):
        user = self.users[user_id]
        log = {}
        log["name"] = user["name"]
        log["start_time"] = user["start_time"]
        log["end_time"] = user["end_time"]
        log["user_code"] = user["user_code"]
        log["conversation"] = user["conversation"]
        file_name = (
            str(user["name"]).replace(" ", "")
            + "-"
            + str(user["user_code"]).replace(" ", "")
            + "-"
            + str(user["start_time"])
        )
        json.dump(
            log,
            open(
                LOGS_PATH + "/" + file_name + ".json",
                "w+",
            ),
        )

    def _log_bot_messages(self, utterance, user_id):
        if utterance == None:
            return
        utterance_dict = json.loads(utterance)
        print(utterance_dict)
        for message in utterance_dict["messages"]:
            if len(message["text"]) != 0:
                self._append_log_entry("albot", message["text"], user_id)

    def replace_name(self, utterance, user_id):
        if utterance == None:
            return None
        dict_utterance = json.loads(utterance)
        new_utterance = {}
        new_utterance["change_phase"] = dict_utterance["change_phase"]
        new_utterance["messages"] = []
        for message in dict_utterance["messages"]:
            new_message = {}
            if "<name>" in message["text"]:
                new_message["text"] = message["text"].replace(
                    "<name>", self.users[user_id]["name"]
                )
                new_message["ui_effect"] = message["ui_effect"]
            else:
                new_message = message
            new_utterance["messages"].append(new_message)
        return json.dumps(new_utterance)

    def generate_utterance(self, intent, user_session_id):
        user = self.users[user_session_id]
        current_state = user["current_state"]
        pending_question = user["pending_question"]
        if user["is_coro_ended"] is None or user["is_coro_ended"] == True:
            # User either does not have a timer or the timer has finished, that means we are no longer in
            # the branch/waiting state so we can behave normally
            (
                new_pending_question,
                next_state,
                utterance_array,
            ) = self.state_machine.input_function(
                intent, current_state, pending_question
            )
            user["current_state"] = next_state
            user["pending_question"] = new_pending_question
            # In the next section we proceed to see if the state we landed in is either a branch or waiting state
            # we start a timer accordingly
            if next_state.value < user["current_state"].value:
                # Means back or home or reset buttons where used
                # user["pending_question"] = None
                user["is_coro_ended"] = None
            if (
                self.state_machine.is_branch(next_state)
                and user["pending_question"] == None
            ):
                self.decide_branch(user_session_id)
            if (
                self.state_machine.is_waiting(next_state)
                and user["pending_question"] == None
            ):
                user["is_coro_ended"] = False
                asyncio.ensure_future(self.branch_child_question(user_session_id))
        elif user["is_coro_ended"] == False:
            # User has a timer and it is on going, meaning i do not update the state cause it will be
            # updated by the timer function and i do not start a new timer
            (
                new_pending_question,
                next_state,
                utterance_array,
            ) = self.state_machine.input_function(
                intent, current_state, pending_question
            )
            user["pending_question"] = new_pending_question
            user["current_state"] = next_state
            if next_state != current_state:
                # Means i moved while i was waiting for a question
                user["is_coro_ended"] == True
                user["question_probability"] = 1
            if next_state.value < user["current_state"].value:
                # Means back or home or reset buttons where used
                # user["pending_question"] = None
                user["is_coro_ended"] = None
        if not bool(utterance_array):
            message = None
        else:
            message = json.dumps(utterance_array)
        return message

    def decide_branch(self, user_session_id):
        rand = random.randint(
            0, 1 * self.users[user_session_id]["question_probability"]
        )
        # if rand == 0:
        # Calling the chatbot_question
        self.users[user_session_id]["is_coro_ended"] = False
        asyncio.ensure_future(self.branch_chatbot_question(user_session_id))
        question_probability = self.users[user_session_id]["question_probability"]
        self.users[user_session_id]["question_probability"] = (
            question_probability * self.state_machine.get_question_multiplier()
        )
        # else:
        # Calling the child question
        # self.users[user_session_id]["is_coro_ended"] = False
        # asyncio.ensure_future(self.branch_child_question(user_session_id))

    async def branch_chatbot_question(self, user_session_id):
        # Decide chatbot question
        await asyncio.sleep(self.state_machine.get_waiting_time())
        if self.users[user_session_id]["is_coro_ended"] == True:
            return
        else:
            intent = self._create_intent("chatbot_question")
            await self.chatbot_sends_message(intent, user_session_id)
            self.users[user_session_id]["is_coro_ended"] = True
            if not self.state_machine.is_cycle(
                self.users[user_session_id]["current_state"]
            ):
                self.users[user_session_id]["question_probability"] = 1
            self.users[user_session_id][
                "current_state"
            ] = self.state_machine.get_next_state(
                self.users[user_session_id]["current_state"]
            )

    async def branch_child_question(self, user_session_id):
        await asyncio.sleep(self.state_machine.get_waiting_time())
        if self.users[user_session_id]["is_coro_ended"] == True:
            return
        else:
            if not self.state_machine.is_cycle(
                self.users[user_session_id]["current_state"]
            ):
                self.users[user_session_id]["question_probability"] = 1
            self.users[user_session_id][
                "current_state"
            ] = self.state_machine.get_next_state(
                self.users[user_session_id]["current_state"]
            )
            intent = self._create_intent("wait_ended")
            await self.chatbot_sends_message(intent, user_session_id)
            self.users[user_session_id]["is_coro_ended"] = True

    async def chatbot_sends_message(self, intent, user_session_id):
        utterance = self.generate_utterance(intent, user_session_id)
        print(utterance)
        self._log_bot_messages(utterance, user_session_id)
        await self.handler.send_message(user_session_id, utterance)

    def _create_intent(self, intent):
        return {"entities": [], "intent": {"confidence": 1, "id": 0, "name": intent}}

    def _nlu_parse(self, text):
        import requests

        data_dict = {"text": text}
        data_json = json.dumps(data_dict)
        response = requests.post("http://localhost:5005/model/parse", data=data_json)
        return json.loads(response.content)
