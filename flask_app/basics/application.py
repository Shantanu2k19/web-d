#export FLASK_APP=application.py


#for date and time
import datetime  

from flask import Flask, render_template

app=Flask(__name__)

#default route
@app.route("/") 
def more():
	return "basic website"  

#adding a route for any string after page address
@app.route("/<string:name>") 
def hello(name):
	return f"hello,{name}!"

#here linking a html file,index.html 
@app.route("/temp") 
def index():
	variable="the headline of the page"
	return render_template("index.html", headline=variable)

#template application
@app.route("/bye")
def bye():
	gg = "goodbye"
	return render_template("index.html",headline=gg)

#for date and time
@app.route("/date")
def datetime():
	now = datetime.datetime.now()
	new_year = now.month ==1 and now.day == 1
	return render_template("datetime.html",new_year=new_year)

#giving list to tempelate to print, also giving link for another html route page
@app.route("/list")
def list():
	names = ["shan","lahu","duhu"]
	return render_template("list.html",names=names)

#redirected here from above
@app.route("/link")
def link():
	return render_template("link.html")
