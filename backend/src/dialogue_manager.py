from state import State
from state_machine import StateMachine
import json 
from threading import Timer
import random
import app

class DialogueManager:
    
    users = {}

    def __init__(self, model):
        self.model = model
        self.state_machine = StateMachine()

    def add_user(self,user_session_id):
        self.users[user_session_id] = {
            'current_state' : State.GREETING,
            'timer' : None,
            'is_timer_ended' : None 
        }
        #The moment the user is added the chatbot greets him and introduces him to the lesson
        intent = {
            'entities' : [],

            'intent': {'confidence': 1,
                        'id': 0,
                        'name': "connected"}
        } 
        print("In dialogue_manager add_user: client connected and added, about to send message ")
        self.chatbot_sends_message(intent,user_session_id)
        


    def del_user(self,user_session_id):
        del self.users[user_session_id]
    
    #msg structure is {"text": text
    #                  "highlighted": objectId
    #                  "user_session_id": sessionId
    #                  "phase" : phaseName
    #                   } 
    def chatbot_receives_message(self,msg,user_id):
        #First the messsage has to be deserialized
        msg = json.load(msg)
        #Control if the text field is empty
        if len(msg.text) != 0:
            #The message is now forwarded to the Rasa NLU and an intent comes back
            intent = self.model.parse(msg.text)
        else:
            #If the length of the text is empty the user acted on the interface selecting an object
            intent = self.select_intent(msg.highlighted)
        
        #Now that i have the intent calculated i can generate a response and move the child on the state machine
        utterance = self.generate_utterance(intent,user_id)
        #TODO: Decide on the on click if we have to give the utterance or return None [Meaning we do not want to answer]
        return utterance
    
    def generate_utterance(self,intent,user_session_id):
        print("In dialogue_manager generate_utterance: beginning of the function ")
        user = self.users[user_session_id]
        current_state = user['current_state']
        if user['is_timer_ended'] is None or user['is_timer_ended'] == True:      
            #User either does not have a timer or the timer has finished, that means we are no longer in 
            # the branch/waiting state so we can behave normally 
            print("In dialogue_manager generate_utterance: about to call input_function ")
            next_state , utterance_array = self.state_machine.input_function(intent,current_state)
            user['current_state'] = next_state
            #In the next section we proceed to see if the state we landed in is either a branch or waiting state
            # we start a timer accordingly
            if self.state_machine.is_branch(next_state):
                self.decide_branch(user_session_id)
            if self.state_machine.is_waiting(next_state):
                user['is_timer_ended'] = False
                user['timer'] = threading.Timer(
                self.state_machine.get_waiting_time(),
                branch_child_question,
                [user_session_id]
                )       
        elif user['is_timer_ended'] == False:
            #User has a timer and it is on going, meaning i do not update the state cause it will be
            # updated by the timer function and i do not start a new timer
            _ , utterance_array = self.state_machine.input_function(intent,current_state)
        
        message = json.dumps(utterance_array)
        msg = {
            'message' : message,
        }
        return msg
    
    def select_intent(self,highlighted):
        intent_name = "clicked_" + highlighted
        intent = {
            'entities' : [
                highlighted
            ],
            'intent': {'confidence': 1,
                        'id': 0,
                        'name': intent_name}
        }
        return intent

    def decide_branch(self,user_session_id):
        rand = random.randint(0,1)
        if rand == 0:
            #Calling the chatbot_question
            self.users[user_session_id]['is_timer_ended'] = False 
            self.users[user_session_id]['timer'] = threading.Timer(0,branch_chatbot_question,[user_session_id])
        else:
            #Calling the child question
            self.users[user_session_id]['is_timer_ended'] = False 
            self.users[user_session_id]['timer'] = threading.Timer(self.state_machine.get_waiting_time(),branch_child_question,[user_session_id]) 
        
    def branch_chatbot_question(self,user_session_id):
        #Has to call the chatbot_sends_message method, 
        intent = "chatbot_question"
        self.chatbot_sends_message(intent,user_session_id)
        self.users[user_session_id]['is_timer_ended'] = True 
        self.users[user_session_id]['current_state'] = self.state_machine.get_next_state(self.users[user_session_id]['current_state'])

    def branch_child_question(self,user_session_id):
        self.users[user_session_id]['is_timer_ended'] = True
        self.users[user_session_id]['current_state'] = self.state_machine.get_next_state(self.users[user_session_id]['current_state'])

    def chatbot_sends_message(self,intent,user_session_id):
        print("In dialogue_manager chatbot_sends_message: ")
        utterance = self.generate_utterance(intent,user_session_id)
        #Call on the app service to send the message
        app.send_message(user_session_id,utterance)


   

        
    
