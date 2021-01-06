from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room
from dialogue_manager import DialogueManager
from model_extractor import load_interpreter

model_directory_path = '../NLUmodule/models'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
dialogueManager = DialogueManager(load_interpreter(model_directory_path))


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

@socketio.on('RECEIVE_MESSAGE')
def client_receive_message(data):
    socketio.send(data.message,room = data.sid)

if __name__ == "__main__":
    app.debug = True 
    socketio.run(app,port = 2345)
    

