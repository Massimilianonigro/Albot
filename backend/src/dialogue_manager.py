from state import State
from state_machine import StateMachine
import json 
import random
import asyncio 

class DialogueManager:
    
    users = {}

    def __init__(self, model,handler):
        self.model = model
        self.state_machine = StateMachine()
        self.handler = handler
    
    async def add_user(self,user_session_id):
        self.users[user_session_id] = {
            'current_state' : State.GREETING,
            'is_coro_ended' : None,
            'pending_question': None 
        }
        #The moment the user is added the chatbot greets him and introduces him to the lesson
        intent = self._create_intent("connected")
        await self.chatbot_sends_message(intent,user_session_id)
        


    def del_user(self,user_session_id):
        del self.users[user_session_id]
    
    #msg structure is {"text": text
    #                  "highlighted": objectId
    #                   } 
    def chatbot_receives_message(self,msg,user_id):
        #First the messsage has to be deserialized
        msg = json.loads(msg)
        #Control if the text field is empty
        if len(msg['text']) != 0:
            #The message is now forwarded to the Rasa NLU and an intent comes back
            print("text received " + str(msg['text']))
            intent = self.model.parse(msg['text'])
        else:
            #If the length of the text is empty the user acted on the interface selecting an object
            obj = msg['highlighted'].replace(" ", "")
            obj = obj.lower()
            print("object clicked "+ obj)
            intent = self._create_intent('clicked_' + obj)
        
        #Now that i have the intent calculated i can generate a response and move the child on the state machine
        utterance = self.generate_utterance(intent,user_id)
        return utterance
    
    def generate_utterance(self,intent,user_session_id):
        user = self.users[user_session_id]
        current_state = user['current_state']
        pending_question = user['pending_question']
        if user['is_coro_ended'] is None or user['is_coro_ended'] == True:      
            #User either does not have a timer or the timer has finished, that means we are no longer in 
            # the branch/waiting state so we can behave normally 
            new_pending_question,next_state , utterance_array = self.state_machine.input_function(intent,current_state,pending_question)
            user['current_state'] = next_state
            user['pending_question'] = new_pending_question
            #In the next section we proceed to see if the state we landed in is either a branch or waiting state
            # we start a timer accordingly
            if self.state_machine.is_branch(next_state):
                self.decide_branch(user_session_id)
            if self.state_machine.is_waiting(next_state):
                user['is_coro_ended'] = False
                asyncio.ensure_future(self.branch_child_question(user_session_id))
        elif user['is_coro_ended'] == False:
            #User has a timer and it is on going, meaning i do not update the state cause it will be
            # updated by the timer function and i do not start a new timer
            new_pending_question ,_ , utterance_array = self.state_machine.input_function(intent,current_state,pending_question)
            user['pending_question'] = new_pending_question
        if len(utterance_array) == 0:
            message = None
        else:
            message = json.dumps(utterance_array)
        return message

    def decide_branch(self,user_session_id):
        rand = random.randint(0,1)
        if rand == 0:
            #Calling the chatbot_question
            self.users[user_session_id]['is_coro_ended'] = False 
            asyncio.ensure_future(self.branch_chatbot_question(user_session_id))
           
        else:
            #Calling the child question
            self.users[user_session_id]['is_coro_ended'] = False 
            asyncio.ensure_future(self.branch_child_question(user_session_id))
    
    async def branch_chatbot_question(self,user_session_id):
        #Decide chatbot question
        intent = self._create_intent("chatbot_question") 
        await self.chatbot_sends_message(intent,user_session_id)
        self.users[user_session_id]['is_coro_ended'] = True 
        self.users[user_session_id]['current_state'] = self.state_machine.get_next_state(self.users[user_session_id]['current_state'])

    async def branch_child_question(self,user_session_id):
        await asyncio.sleep(self.state_machine.get_waiting_time())
        self.users[user_session_id]['current_state'] = self.state_machine.get_next_state(self.users[user_session_id]['current_state'])
        intent = self._create_intent("wait_ended")
        await self.chatbot_sends_message(intent,user_session_id)
        self.users[user_session_id]['is_coro_ended'] = True

    async def chatbot_sends_message(self,intent,user_session_id):
        utterance = self.generate_utterance(intent,user_session_id)
        await self.handler.send_message(user_session_id,utterance)
    
    def _create_intent(self,intent):
       return {
                'entities' : [],

                'intent': {'confidence': 1,
                            'id': 0,
                            'name': intent}
               }  



   

        
    
