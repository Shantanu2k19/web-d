from flask import Flask, render_template, request, session
from flask_session import Session
#session data stored about server side
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#notes global variable,hence common to all the users on server
#notes = []
#should be avoided, hence concept of sessions

@app.route("/", methods=["GET", "POST"])
def index():
	if session.get("notes") is None: #due to these 2 lines, the new notes data will not be overwritten by older one
		session["notes"]=[]  #my particular session has empty notes list

	if request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)
	return render_template("index.html", notes=session["notes"])
