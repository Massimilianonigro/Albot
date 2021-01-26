import asyncio
import websockets
import dialogue_manager as dm
from model_extractor import load_interpreter

model_directory_path = './NLUmodule/models'
connected = {}
counter = 0

async def handler(websocket, path):
    while True:
        try:
            if websocket not in connected.values():
                await register(websocket)
            message = await websocket.recv()
            await handle_message(websocket,message)
        except websockets.ConnectionClosed:
            await unregister(websocket)
            break 

async def register(websocket):
    counter = counter + 1 
    connected[counter] = websocket
    dialogueManager.add_user(counter)


async def unregister(websocket):
    for key, item in connected.items(): 
    if item is websocket: 
        del connected[key] 
        break

async def handle_message(websocket,message)
    user_id = -1 
    for key, item in connected.items(): 
    if item is websocket: 
        user_id = key
        break 
    #TODO: Expeption if the user_id = -1 
    response = dialogueManager.chatbot_receives_message(message,user_id)
    websocket.send(response)

#Check how to behave with the other send/recv 
def send_message(user_id,message):
    websocket = connected[user_id]
    websocket.send(message)
    
    
if __name__ == "__main__":
    dialogueManager = dm.DialogueManager(load_interpreter(model_directory_path))
    start_server = websockets.serve(handler, 'localhost', 2345)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    
