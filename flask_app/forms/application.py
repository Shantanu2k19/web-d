from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET","POST"]) #submitting data via post method
def hello():
	if request.method == "GET":
		return "please submit the form"
	else:
	    name = request.form.get("name") #access form and get name
	    return render_template("hello.html", name=name)
