# CODE 1


#defining structure(rows and columns of the tables to be created)
#it is used by create.py to create tables
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class flight(db.Model):  #flight is inheriting from model database of sqlAlchemy
	__tablename__ = "flights" #table name in database
	id = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String, nullable=False)
	destination = db.Column(db.String, nullable=False)
	duration = db.Column(db.Integer, nullable=False)

class passengers(db.Model):
	__tablename__ = "passengers"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	#foreign key, flight_key is gonna reference id column from flight table
	flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
