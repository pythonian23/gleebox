from replit import db

import crypto

from flask import Flask, render_template
from flask_socketio import SocketIO
import json


app = Flask(__name__)

app.config["SECRET_KEY"] = "aaack"
socketio = SocketIO(app)


@socket_io.on("connect")
def connect():
    print("socket connected")

@socket_io.on("join")
def join(data):
    flask_socketio.join_room(data["room"])

@socket_io.on("leave")
def leave(data):
    flask_socketio.leave_room(data["room"])

@socketio.on("message")
def handle_json(dat):
    json.loads(dat)

if __name__ == "__main__":
    socketio.run(app) #  PORT: 5000