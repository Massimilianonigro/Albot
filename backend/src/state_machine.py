from state import state
import json

class StateMachine:
    def __init__(self):
        self.load_json()

    def load_json(self):
        with open("../resources/utterances.json", "r") as read_file:
            self.utterances = json.load(read_file)
        with open("../resources/ingredients_list.json", "r") as read_file:
            self.ingredients_list = json.load(read_file)

    def input_function(self,intent,current_state):
        next_state , utterance_array = self.options[current_state](self,intent,current_state)
        return next_state , utterance_array
    
    def greeting(self,intent,current_state): 
        utterance_array = []
        next_state = current_state
        if intent['intent']['name'] == "connected" :
            utterance_array.append(self.utterances['greeting'].choice())
            utterance_array.append(self.utterances['introduction_or_practice'].choice())
        else if intent['intent']['name'] == "clicked_practice":
            next_state = State.PRACTICE_COLLECTING
            utterance_array.append(self.utterances['practice_explanation'].choice())
        else if intent['intent']['name'] == "clicked_introduction":
            next_state = State.INTRODUCTION_START
            utterance_array.append(self.utterances['introduction_explanation'].choice())
        else if intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(self.utterances['fallback'].choice())
        return next_state , utterance_array
            
    def introduction_start(self,intent,current_state):
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        else if intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(self.utterances['fallback'].choice())
        return next_state,utterance_array

    def acid_selection(self,intent,current_state):
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
            return next_state,utterance_array
        if intent['intent']['name'] == "clicked_next":
            utterance_array.append(self.utterances['base_selection'].choice())
            next_state = State.BASE_SELECTION
        else if intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(self.utterances['fallback'].choice())
        return next_state,utterance_array
    
    def base_selection(self,intent,current_state):
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
            return next_state,utterance_array
        if intent['intent']['name'] == "clicked_next":
            utterance_array.append(self.utterances['guided_reasoning_explanation'].choice())
            next_state = State.GUIDED_REASONING
        else if intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(self.utterances['fallback'].choice())
        return next_state,utterance_array
    
    def guided_reasoning(self,intent,current_state):
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == "chatbot_question":
            utterance_array.append(self.utterances['chatbot_question'].choice()) 
        else if intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(self.utterances['fallback'].choice())
        return next_state, utterance_array
    
    def guided_pouring(self,intent,current_state):
        #This state loops until user clicks next
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == "chatbot_question":
            utterance_array.append(self.utterances['chatbot_question'].choice())  
        else if intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(self.utterances['fallback'].choice())
        else if intent['intent']['name'] == "clicked_next":
            next_state = State.PRACTICE_COLLECTING
            utterance_array.append(self.utterances['practice_collecting_explanation'].choice())
        else if intent['intent']['name'] != "clicked_next" and intent['intent']['name'][0:7] == "clicked":
            utterance_array.append(self.utterances['color_change_exclamation'].choice())
        return next_state, utterance_array
    
    def practice_collecting(self,intent,current_state):
        utterance_array = []
        next_state = current_state
        question_explanation = self.general_questions(intent)
        if question_explanation != None:
            utterance_array.append(question_explanation)
        if intent['intent']['name'] == "clicked_next":
            next_state = State.PRACTICE_CYCLE
            utterance_array.append(self.utterances['practice_collecting_explanation'].choice())
        else if intent['intent']['name'] == "nlu_fallback":
            utterance_array.append(self.utterances['fallback'].choice())
        return next_state, utterance_array

    def practice_cycle(self,intent,current_state):
        

    #Answer general questions of the user that can be done over all the interaction, takes in an intent and gives back a string
    def general_questions(self,intent):
        if intent['intent']['name'] == "inform_ph":
            return self.utterances['ph_explanation'].choice()
        elif intent['intent']['name'] == "inform_ph_property":
            if intent['entities']["value"][0:4] == 'base':
                return self.utterances['base_explanation'].choice()
            elif intent['entities']["value"][0:4] == 'acid':
                return self.utterances['acid_explanation'].choice()
            else:
                return "Did not understand the ph entity you want info about"
        elif intent['intent']['name'] == "inform_cabbage_solution":
            return self.utterances['cabbage_solution_explanation'].choice()
        elif intent['intent']['name'] == "inform_ingredient_property":
            ingredient = intent['entities']["value"]
            if ingredient in self.ingredients_list: 
                #Check on ph to deliver explanation
                ingredient_ph = self.ingredients_list[ingredient]['ph']
                explanation = "The " + ingredient + "has a ph of " + ingredient_ph 
                if ingredient_ph == 7:
                    explanation = explanation + "and is thus a neutral substance." +  self.utterances['properties_neutral_ingredient'].shuffle()
                elif ingredient_ph < 7:
                    explanation = explanation + "and is thus an acid substance." +  self.utterances['properties_acid_ingredient'].shuffle()
                elif ingredient_ph > 7:
                    explanation = explanation + "and is thus a basic substance." +  self.utterances['properties_base_ingredient'].shuffle()
                return explanation
            else:
                return "Ingredient not recognized"
        else:
            return None

    #Determines if at the beginning of the state there is a branch between chatbot or child question
    def is_branch(self,state):
        if state in self.optional_states:
            return True 
        else 
            return False

    def is_waiting(self,state):
        if state in self.waiting_states:
            return True 
        else 
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
            State.INTRODUCTION_START : introduction_start
            State.ACID_SELECTION : acid_selection,
            State.BASE_SELECTION : base_selection,
            State.WAITING : waiting,
            State.GUIDED_REASONING : guided_reasoning,
            State.GUIDED_POURING : guided_pouring,
            State.PRACTICE_COLLECTING : practice_collecting,
            State.PRACTICE_CYCLE : practice_cycle
        }
    optional_states = [State.GUIDED_REASONING,State.GUIDED_POURING,State.PRACTICE_CYCLE]
    waiting_states = [State.INTRODUCTION_START]
    utterances = {}
    waiting_time = 3 