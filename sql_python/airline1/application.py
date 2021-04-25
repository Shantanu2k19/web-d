from flask import Flask, render_template, request, jsonify 
from models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://zodiac_sql:shan@localhost/postgres")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

"""
here, 
Flight : name of class for creating table
Passengers : name of class for creating passengers table

flightss : object/variable used to access data 
"""

@app.route("/")
def index():
    flightss = Flight.query.all()
    return render_template("index.html", flights=flightss)


@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight with that id.")

    # Adding a passenger.

    #way 1, using python replacement of sql, like we did previously
    passenger = Passenger(name=name, flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()

    #way 2, using class,
    #flight.add_passenger(name) #uncomment to use 2nd way
    #here, add_passenger is a definition added in the class Flight(models.py)
    #takes name,adds and commit it

    
    return render_template("success.html")


@app.route("/flights")
def flights():
    """List all flights."""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")

    # Get all passengers.

    #way 1
    #passengers = Passenger.query.filter_by(flight_id=flight_id).all()

    #way2 : using relationships(check models.py)
    passengers = flight.passengers

    #printing fetched details
    return render_template("flight.html", flight=flight, passengers=passengers)




#adding a route for API
@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    """Return details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"error": "Invalid flight_id"}), 422
        #jsonify function used to return jason object {}, 422-> pass back an error status code


    # Get all passengers.
    passengers = flight.passengers
    #create a list
    names = []
    for passenger in passengers:
        names.append(passenger.name)
    #add all passengers to the list 

    #return jason object
    return jsonify({
            "origin": flight.origin,
            "destination": flight.destination,
            "duration": flight.duration,
            "passengers": names
        })
