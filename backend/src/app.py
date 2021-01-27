import asyncio
import websockets
import dialogue_manager as dm
from model_extractor import load_interpreter

model_directory_path = './NLUmodule/models'

class Handler():
    def __init__(self):
        self.counter = 0
        self.connected = {}
        self.dialogue_manager =  dm.DialogueManager(load_interpreter(model_directory_path),self)
    
    async def handle(self,websocket,path):
        while True:
            try:
                if websocket not in self.connected.values():
                    await self.register(websocket)
                message = await websocket.recv()
                await self.handle_message(websocket,message)
            except websockets.ConnectionClosed:
                await self.unregister(websocket)
                break 

    async def register(self,websocket):
        print("Registering user")
        self.counter = self.counter + 1 
        self.connected[self.counter] = websocket
        await self.dialogue_manager.add_user(self.counter)


    async def unregister(self,websocket):
        for key, item in self.connected.items(): 
            if item is websocket: 
                del self.connected[key] 
                break

    async def handle_message(self,websocket,message):
        user_id = -1 
        for key, item in self.connected.items(): 
            if item is websocket: 
                user_id = key
                break 
        #TODO: Expeption if the user_id = -1 
        response = self.dialogue_manager.chatbot_receives_message(message,user_id)
        print(response)
        await websocket.send(response)

    #Check how to behave with the other send/recv 
    async def send_message(self,user_id,message):
        websocket = self.connected[user_id]
        print(message)
        await websocket.send(message)

    
if __name__ == "__main__":
    handler = Handler()
    start_server = websockets.serve(handler.handle, 'localhost', 2345)
    print("Server started on localhost:2345")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
   
