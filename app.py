import time

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def api():
    print("打开页面")
    return render_template("index.html")


@app.route('/tow/')
def api2():
    print("打开页面")
    return render_template("index2.html")


@app.route('/tow2/')
def api3():
    print("打开页面")
    return render_template("index3.html")


def ack():
    print('message was received!')


@socketio.on('my event')
def handle_my_custom_event(json):
    Room = json['room']
    send(json, room=Room);

    print('received json: ' + str(json)+'room:'+Room)


@socketio.on('join')
def on_join(data):
    username = data['username']
    Room = data['room']
    join_room(Room)
    send({'content':Room}, room=Room)

if __name__ == '__main__':
    socketio.run(app)
