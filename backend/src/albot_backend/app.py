import asyncio
import websockets
import albot_backend.dialogue_manager as dm
from pathlib import Path

"""[summary] Handler class takes care of the communication with the front-end leveraging websocket
[extended_summary] Handler takes care of connected users, and relays all the interaction of the users with the chatbot to the dialogue manager.
Which formulates a response that is then sent back.
:raises RuntimeError: When user_id handling does not go correctly. [description]
"""


class Handler:
    def __init__(self):
        self.counter = 0
        self.connected = {}
        self.dialogue_manager = dm.DialogueManager(self)

    async def handle(self, websocket, path):
        while True:
            try:
                if websocket not in self.connected.values():
                    await self.register(websocket)
                message = await websocket.recv()
                await self.handle_message(websocket, message)
            except websockets.ConnectionClosed:
                await self.unregister(websocket)
                break

    async def register(self, websocket):
        print("Registering user")
        self.counter = self.counter + 1
        self.connected[self.counter] = websocket
        await self.dialogue_manager.add_user(self.counter)

    async def unregister(self, websocket):
        for key, item in self.connected.items():
            if item is websocket:
                del self.connected[key]
                break

    async def handle_message(self, websocket, message):
        user_id = -1
        for key, item in self.connected.items():
            if item is websocket:
                user_id = key
                break
        if user_id == -1:
            raise RuntimeError("Message handled is sent from unregistered user")
        response = self.dialogue_manager.chatbot_receives_message(message, user_id)
        if response != None:
            print("sending " + str(response))
            await websocket.send(response)

    # Check how to behave with the other send/recv
    async def send_message(self, user_id, message):
        websocket = self.connected[user_id]
        if message != None:
            await websocket.send(message)


def main():
    try:
        handler = Handler()
        start_server = websockets.serve(handler.handle, "0.0.0.0", 2345)
        print("Server started on localhost:2345")
        asyncio.get_event_loop().run_until_complete(start_server)

        asyncio.get_event_loop().run_forever()
    except Exception as e:
        print(e)
        main()


if __name__ == "__main__":
    main()
