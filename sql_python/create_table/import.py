#CODE 3

#adding(importing) data from csv fileimport csv
import os, csv

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://zodiac_sql:shan@localhost/postgres")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        obj = flight(origin=origin, destination=destination, duration=duration) #flight is the name of the class(model.py)
        #flight object
        db.session.add(obj) #equivalent to insert command
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.session.commit() #apply changes

if __name__ == "__main__":
    with app.app_context():
        main()
