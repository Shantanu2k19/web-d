import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    #added relationships (its all about simplifying the syntax)
    passengers = db.relationship("Passenger", backref="flight", lazy=True)
    #relating both tables, flight is the keyword to access the passenger details
    #lazy evaluate tells database to not fetch the passengers info unless called(effeciency bonus)
    """ using this
    select * from flights join passengers on flight.id = passengers.flight_id where passenegrs.name = 'shan';
    can be converted to 
    passengers.query.filter_by(name='shan')\.first().flight()
    """

    def add_passenger(self, name):
        p = Passenger(name=name, flight_id=self.id)  #self is individual flight here
        db.session.add(p)
        db.session.commit()


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
