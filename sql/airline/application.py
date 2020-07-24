import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
 
engine = create_engine("postgres://zodiac:elonmusk@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)
    

@app.route("/book", methods=["POST"])  #used in index.html
def book():
    """Book a flight."""

    # Get form information from thr form
    name = request.form.get("name") 
    if name == "":
        return render_template("error.html", message="Name required!")
    #try and except to manage errors
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists.
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0: 
        return render_template("error.html", message="No such flight with that id.")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
            {"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("success.html")


#added routes to view the list of flight  
@app.route("/flights")
def flights():
    flights = db.execute("select * from flights").fetchall()
    return render_template("flights.html", flights=flights)


#added route to view the passengers on a certain flight
@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    # Make sure flight exists.
    flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message="No such flight.")

    # Get all passengers.
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)