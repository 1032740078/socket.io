import time
#参考链接:https://www.jianshu.com/p/11d45bfd03ed
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'#key密码
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
    send(json, room=Room);#room:广播到对应的房间名

    print('received json: ' + str(json)+'room:'+Room)


@socketio.on('join')
def on_join(data):
    Room = data['room']#房间名
    join_room(Room)#加入对应房间
    send({'content':Room}, room=Room)

if __name__ == '__main__':
    socketio.run(app)
