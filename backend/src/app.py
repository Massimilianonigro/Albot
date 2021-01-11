from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room
import dialogue_manager as dm
from model_extractor import load_interpreter

model_directory_path = './NLUmodule/models'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app,cors_allowed_origins="*",always_connect=True)


# Flaks or socket.Io layer can be added here

@socketio.on('connect')
def client_connect():
    print("client connected")
    dialogueManager.add_user(request.sid)
    
@socketio.on('disconnect')
def client_disconnect():
    print('client disconnect')
    dialogueManager.del_user(request.sid)
    
#TODO: Check how to emit to specific client
@socketio.on('SEND_MESSAGE')
def client_send_message(data):
    print('client send message')
    data['sid'] = request.sid
    answer = dialogueManager.chatbot_receives_message(data)
    socketio.send(answer.message,room = answer.sid)


def client_receive_message(data):
    print("sending the message ")
    socketio.emit('MESSAGE',data['message'],room = data['sid'])

if __name__ == "__main__":
    app.debug = True 
    dialogueManager = dm.DialogueManager(load_interpreter(model_directory_path))
    socketio.run(app,port = 2345)
    
    
    

