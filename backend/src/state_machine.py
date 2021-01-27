from state import State
import json
import random as rand

class StateMachine:
    def __init__(self):
        self.load_json()

    def load_json(self):
        with open("./resources/utterances.json", "r") as read_file:
            self.utterances = json.load(read_file)
        with open("./resources/ingredients_list.json", "r") as read_file:
            self.ingredients_list = json.load(read_file)['ingredients']

    def input_function(self,intent,current_state):
        print("In state_machine input_function: " + str(current_state) + ", intent recognized is: " + str(intent))
        next_state , utterance_array = self.options[current_state](self,intent,current_state)
        return next_state , utterance_array
    
    def greeting(self,intent,current_state): 
        utterance_array = []
        next_state = current_state
        if intent['intent']['name'] == "connected" :
            utterance_array.append(rand.choices(self.utterances['greeting'])[0])
            utterance_array.append(rand.choices(self.utterances['introduction_or_practice'])[0])
        elif intent['intent']['name'] == "clicked_practice":
            next_state = State.PRACTICE_COLLECTING
            utterance_array.append(rand.choices(self.utterances['practice_explanation'])[0])
        elif intent['intent']['name'] == "clicked_introduction":
            next_state = State.INTRODUCTION_START
            utterance_array.append(rand.choices(self.utterances['introduction_explanation'])[0])
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(rand.choices(self.utterances['fallback'])[0])
        return next_state , utterance_array
            
    def introduction_start(self,intent,current_state):
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(rand.choices(self.utterances['fallback'])[0])
        return next_state,utterance_array

    def acid_selection(self,intent,current_state):
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
            return next_state,utterance_array
        if intent['intent']['name'] == "clicked_next":
            utterance_array.append(rand.choices(self.utterances['base_selection'])[0])
            next_state = State.BASE_SELECTION
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(rand.choices(self.utterances['fallback'])[0])
        return next_state,utterance_array
    
    def base_selection(self,intent,current_state):
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
            return next_state,utterance_array
        if intent['intent']['name'] == "clicked_next":
            utterance_array.append(rand.choices(self.utterances['guided_reasoning_explanation'])[0])
            next_state = State.GUIDED_REASONING
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(rand.choices(self.utterances['fallback'])[0])
        return next_state,utterance_array
    
    def guided_reasoning(self,intent,current_state):
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == "chatbot_question":
            utterance_array.append(rand.choices(self.utterances['chatbot_question'])[0]) 
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(rand.choices(self.utterances['fallback'])[0])
        return next_state, utterance_array
    
    def guided_pouring(self,intent,current_state):
        #This state loops until user clicks next
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == "chatbot_question":
            utterance_array.append(rand.choices(self.utterances['chatbot_question'])[0])  
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(rand.choices(self.utterances['fallback'])[0])
        elif intent['intent']['name'] == "clicked_next":
            next_state = State.PRACTICE_COLLECTING
            utterance_array.append(rand.choices(self.utterances['practice_collecting_explanation'])[0])
        elif intent['intent']['name'] != "clicked_next" and intent['intent']['name'][0:7] == "clicked":
            utterance_array.append(rand.choices(self.utterances['color_change_exclamation'])[0])
        return next_state, utterance_array
    
    def practice_collecting(self,intent,current_state):
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == "clicked_next":
            next_state = State.PRACTICE_CYCLE
            utterance_array.append(rand.choices(self.utterances['practice_collecting_explanation'])[0])
        elif intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(rand.choices(self.utterances['fallback'])[0])
        return next_state, utterance_array

    def practice_cycle(self,intent,current_state):
        pass

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
        if state == State.GUIDED_POURING:
            return state
        else:
            return State(state.value + 1)
    

    ingredients_list = {}
    options = {
            State.GREETING : greeting,
            State.INTRODUCTION_START : introduction_start,
            State.ACID_SELECTION : acid_selection,
            State.BASE_SELECTION : base_selection,
            State.GUIDED_REASONING : guided_reasoning,
            State.GUIDED_POURING : guided_pouring,
            State.PRACTICE_COLLECTING : practice_collecting,
            State.PRACTICE_CYCLE : practice_cycle
        }
    optional_states = [State.GUIDED_REASONING,State.GUIDED_POURING,State.PRACTICE_CYCLE]
    waiting_states = [State.INTRODUCTION_START]
    utterances = {}
    waiting_time = 3