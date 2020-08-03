#socket.io 
#real time changes without reloading the page
#library used : SocketIO to use web sockets inside flask app

import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

#when socket detect event 'submit vote', this code runs
@socketio.on("submit vote")
def vote(data):
    selection = data["selection"] #take data
    emit("announce vote", {"selection": selection}, broadcast=True)
    #broadcast that vote using emit() to everyone
