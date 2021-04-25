#CODE 2


#creating tables just using python code
import os

from flask import Flask, render_template, request
from models import *
#import * mean import everything

#here we locating the database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://zodiac_sql:shan@localhost/postgres")
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") #original code, above is changed one

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) #tie this database with this application

def main():
    db.create_all()
    #it will create tables based on what we have in models file
    #we do not need to create table using commands as we did previously

if __name__ == "__main__": 
    with app.app_context():
        main()
