from state import State
import json
import random as rand
from question_handler import QuestionHandler

class StateMachine:
    def __init__(self):
        self.load_json()
        self.question_handler = QuestionHandler()

    def load_json(self):
        with open("./resources/utterances.json", "r") as read_file:
            self.utterances = json.load(read_file)
        with open("./resources/ingredients_list.json", "r") as read_file:
            self.ingredients_list = json.load(read_file)['ingredients']

    def input_function(self,intent,current_state,pending_question):
        print("In state_machine input_function: " + str(current_state) + ", intent recognized is: " + str(intent))
        pending_question , next_state , utterance_array = self.options[current_state](self,intent,current_state,pending_question)
        return pending_question, next_state , utterance_array
    
    def greeting(self,intent,current_state,pending_question): 
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        if intent['intent']['name'] == "connected" :
            utterance_array =  self._append_utterances(utterance_array,['greeting','introduction_or_practice'])
        elif intent['intent']['name'] == "clicked_practice":
            next_state = State.PRACTICE_COLLECTING
            utterance_array = self._append_utterances(utterance_array,['practice_explanation'])
        elif intent['intent']['name'] == "clicked_introduction":
            next_state = State.INTRODUCTION_START
            utterance_array = self._append_utterances(utterance_array,['introduction_explanation'])
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback'])
        return new_pending_question, next_state , utterance_array
            
    def introduction_start(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback'])
        return new_pending_question,next_state,utterance_array

    def acid_selection(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
            return next_state,utterance_array
        if intent['intent']['name'] == "wait_ended":
            utterance_array = self._append_utterances(utterance_array,['acid_selection'])
        if intent['intent']['name'] == "clicked_next":
            utterance_array = self._append_utterances(utterance_array,['base_selection'])
            next_state = State.BASE_SELECTION
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback'])
        return new_pending_question,next_state,utterance_array
    
    def base_selection(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
            return next_state,utterance_array
        if intent['intent']['name'] == "clicked_next":
            utterance_array = self._append_utterances(utterance_array,['guided_reasoning_explanation'])
            next_state = State.GUIDED_REASONING
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback'])
        return new_pending_question,next_state,utterance_array
    
    def guided_reasoning(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == "chatbot_question":
            new_pending_question = self.question_handler.get_random_question("other")
            question = self.question_handler.get_question_by_id(new_pending_question)
            utterance_array.append(question)
        elif intent['intent']['name'] == "nlu_fallback":
           utterance_array = self._append_utterances(utterance_array,['fallback'])
        return new_pending_question,next_state, utterance_array
    
    def guided_pouring(self,intent,current_state,pending_question):
        #This state loops until user clicks next
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == "chatbot_question":
            new_pending_question = self.question_handler.get_random_question("other")
            question = self.question_handler.get_question_by_id(new_pending_question)
            utterance_array.append(question)
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback'])
        elif intent['intent']['name'] == "clicked_next":
            next_state = State.PRACTICE_COLLECTING
            utterance_array = self._append_utterances(utterance_array,['practice_explanation'])
        elif intent['intent']['name'] != "clicked_next" and intent['intent']['name'][0:7] == "clicked":
            utterance_array = self._append_utterances(utterance_array,['color_change_exclamation'])
        return new_pending_question,next_state, utterance_array
    
    def practice_collecting(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == "clicked_next":
            next_state = State.PRACTICE_CYCLE
            utterance_array = self._append_utterances(utterance_array,['practice_collecting_explanation'])
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback'])
        return new_pending_question,next_state, utterance_array

    def practice_cycle(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == 'chatbot_question':
            new_pending_question = self.question_handler.get_random_question("gamification")
            question = self.question_handler.get_question_by_id(new_pending_question)
            utterance_array.append(question)
            next_state = State.PRACTICE_CHATBOT_QUESTION 
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback'])
        return new_pending_question,next_state,utterance_array

    def practice_chatbot_question(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback'])
            return new_pending_question,next_state,utterance_array
        elif intent['intent']['name'] == "clicked_Try Again":
            question_id = self.question_handler.get_random_question("gamification")
            question = self.question_handler.get_question_by_id(question_id)
            new_pending_question = question_id
            utterance_array.append(question)
        elif intent['intent']['name'] == "clicked_Continue":
            next_state = State.PRACTICE_INFORMATION
        if self.question_handler.get_category_by_id(pending_question) == "gamification":
            if self.question_handler.verify_answer(pending_question,intent['intent']['name']):
                utterance_array = self._append_utterances(utterance_array,['chatbot_appreciation','grant_points'])
                new_pending_question = None
            else:
                utterance_array = self._append_utterances(utterance_array,['wrong_answer','try_again'])
                explanation = self.question_handler.get_explanation_by_id(pending_question)
                utterance_array.append(explanation)
                new_pending_question = None
        

    def practice_child_question(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback']) 
        return new_pending_question,next_state,utterance_array

    def practice_information(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
            return next_state,utterance_array
        if intent['intent']['name'] == "wait_ended":
            utterance_array = self._append_utterances(utterance_array,['practice_information']) 
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback']) 
        return new_pending_question,next_state,utterance_array

    def practice_reset(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
            return next_state,utterance_array
        if intent['intent']['name'] == "wait_ended":
            utterance_array = self._append_utterances(utterance_array,['practice_reset']) 
        elif intent['intent']['name'] == "clicked_reset":
            utterance_array = self._append_utterances(utterance_array,['practice_explanation']) 
            next_state = State.PRACTICE_CYCLE
        elif intent['intent']['name'] == "clicked_next":
            next_state = State.PRACTICE_CLARIFICATION
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback']) 
        return new_pending_question,next_state,utterance_array 

    def practice_clarification(self,intent,current_state,pending_question):
        utterance_array = []
        new_pending_question = pending_question
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == 'chatbot_question':
            new_pending_question = self.question_handler.get_random_question("other")
            question = self.question_handler.get_question_by_id(new_pending_question)
            utterance_array.append(question)
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array = self._append_utterances(utterance_array,['fallback'])
        elif intent['intent']['name'] == "wait_ended":
            utterance_array = self._append_utterances(utterance_array,['end_experience'])
        if self.question_handler.get_category_by_id(pending_question) == "other":
            if self.question_handler.verify_answer(pending_question,intent['intent']['name']):
                utterance_array = self._append_utterances(utterance_array,['chatbot_appreciation','grant_points'])
                new_pending_question = None
            else:
                utterance_array = self._append_utterances(utterance_array,['wrong_answer'])
                explanation = self.question_handler.get_explanation_by_id(pending_question)
                utterance_array.append(explanation)
                utterance_array = self._append_utterances(utterance_array,['wrong_answer']) 
                new_pending_question = No

        return new_pending_question,next_state,utterance_array

    #Answer general questions of the user that can be done over all the interaction, takes in an intent and gives back a string
    def general_questions(self,intent):
        if intent['intent']['name'] == "inform_ph":
            return rand.choices(self.utterances['ph_explanation'])[0]
        elif intent['intent']['name'] == "inform_ph_property":
            if intent['entities'][0]["value"][0:4] == 'base':
                return rand.choices(self.utterances['base_explanation'])[0]
            elif intent['entities'][0]["value"][0:4] == 'acid':
                return rand.choices(self.utterances['acid_explanation'])[0]
            else:
                return "Did not understand the ph entity you want info about"
        elif intent['intent']['name'] == "inform_cabbage_solution":
            return rand.choices(self.utterances['cabbage_solution_explanation'])[0]
        elif intent['intent']['name'] == "inform_ingredient_property":
            ingredient = intent['entities'][0]["value"]
            ingredient_is_in_list = False
            ingredient_ph = -1
            for i in self.ingredients_list:
                if i['name'] == ingredient:
                    ingredient_is_in_list = True 
                    ingredient_ph = i['ph']
                    break 
            if ingredient_is_in_list: 
                #Check on ph to deliver explanation
                explanation = "The " + ingredient + "has a ph of " + str(ingredient_ph)
                if ingredient_ph == 7:
                    explanation = explanation + "and is thus a neutral substance." +  rand.choices(self.utterances['properties_neutral_ingredient'])[0]
                elif ingredient_ph < 7:
                    explanation = explanation + "and is thus an acid substance." +  rand.choices(self.utterances['properties_acid_ingredient'])[0]
                elif ingredient_ph > 7:
                    explanation = explanation + "and is thus a basic substance." +  rand.choices(self.utterances['properties_base_ingredient'])[0]
                return explanation
            else:
                return "Ingredient not recognized"
        else:
            return None

    #Determines if at the beginning of the state there is a branch between chatbot or child question
    def is_branch(self,state):
        if state in self.optional_states:
            return True 
        else:
            return False

    def is_waiting(self,state):
        if state in self.waiting_states:
            return True 
        else:
            return False 

    def get_waiting_time(self):
        return self.waiting_time

    def get_next_state(self,state):
        if state in self.cycle_states:
            return state
        else:
            return State(state.value + 1)
    
    def _append_utterances(self,array,utterance_list):
        for utterance in utterance_list:
            array.append(rand.choices(self.utterances[utterance])[0])
        return array

    ingredients_list = {}
    options = {
            State.GREETING : greeting,
            State.INTRODUCTION_START : introduction_start,
            State.ACID_SELECTION : acid_selection,
            State.BASE_SELECTION : base_selection,
            State.GUIDED_REASONING : guided_reasoning,
            State.GUIDED_POURING : guided_pouring,
            State.PRACTICE_COLLECTING : practice_collecting,
            State.PRACTICE_CYCLE : practice_cycle,
            State.PRACTICE_CHATBOT_QUESTION : practice_chatbot_question,
            State.PRACTICE_CHILD_QUESTION : practice_child_question,
            State.PRACTICE_INFORMATION : practice_information,
            State.PRACTICE_RESET : practice_reset,
            State.PRACTICE_CLARIFICATION : practice_clarification
        }
    cycle_states = [State.GUIDED_POURING,State.PRACTICE_CHATBOT_QUESTION,State.PRACTICE_CLARIFICATION]
    optional_states = [State.GUIDED_REASONING,State.GUIDED_POURING,State.PRACTICE_CYCLE,State.PRACTICE_CLARIFICATION]
    waiting_states = [State.INTRODUCTION_START,State.PRACTICE_CHILD_QUESTION,State.PRACTICE_INFORMATION]
    utterances = {}
    waiting_time = 3