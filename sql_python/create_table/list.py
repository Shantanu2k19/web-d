#CODE 4

#printing data: earlier sql used to print with python, here only python is used
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://zodiac_sql:shan@localhost/postgres")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#prints all the flight table details
def main():    
    flights = flight.query.all()  #flights: object, flight: class name
    for var in flights:  #var is of type list
        print(f"{var.id} : {var.origin} to {var.destination}, {var.duration} minutes.")


    print("\nsql commands python replacements")
    gg = flight.query.filter_by(origin="paris").all()
    for var in gg:
        print(f"{var.id} : {var.origin} to {var.destination}, {var.duration} minutes.")

    nah = flight.query.filter_by(origin='paris').count()
    print("\nnumber of flights with origin as paris : ",nah)

    #ok = flight.query.filter_by(id=1).first()
    idd = 1
    ok = flight.query.get(idd)
    if ok is None: 
        print(f"no flights with id {idd}")
    else:
        print(f"\nflight with id {idd} : ",ok.origin, " to destination :",ok.destination)

"""
    var=flight.query.get(16)
    db.session.delete(var)
    print("\n deleted flight with id:16\n")
    flights = flight.query.all()  #flights: object, flight: class name
    for var in flights:  #var is of type list
        print(f"{var.id} : {var.origin} to {var.destination}, {var.duration} minutes.")

    #db.session.commit(), this will apply changes \, i.e deletion will be in data base
    #commented, hence changes will not be applied to db like deleteion etc
"""
if __name__ == "__main__":
    with app.app_context():
        main()

"""
SEQLALCHMY _ PYTHON EQUIVALENT FOR SQL COMMANDS
here the table name is : flights
class name for creating table : flight
object name : obj

creating object :: obj = flight.query.all()

select * from flights;
flight.query.all();

select * from flights where origin = 'paris';
flight.query.filter_by(origin="paris").all()

select * from flights where origin = 'paris' limit 1;
flight.query.filter_by(origin="paris").first()

select count(*) from flights where origin = 'paris';
flight.query.filter_by(origin='paris').count()

select * from flights where id=28;
flight.query.filter_by(id=28).first()
flight.query.get(28)   #same thing

update flights set duration = 280 where id = 6;
flight=flight.query.get(6)
flight.duration=280

delete from flights where id=2;
var=flight.query.get(28)
db.session.delete(var)

commit;
db.session.commit()

select * from flights order by origin;
flight.querry.order_by(flight.origin).all()

select * from flights order by origin DESC;
flight.query.order_by(flight.origin.desc()).all()

select * from flights where origin != 'paris';
flight.query.filter(flight.origin != "paris").all()

select * from flights where origin like '%a%'
flights.query.filter(flights.origin.like("%a%")).all()

select * from flights where origin in ('tokyo','paris');
flight.query.filter(flight.origin.in_(["tokyo","paris"]).all()

select * from flights where origin = 'paris' and duration>500;
flight.query.fliter(and_(flight.origin=="paris",flight.duration>500)).all()

select * from flights where origin='paris' or duration>500;
flights.query.filter(or_(flight.origin=="paris", flight.duration>500)).all()

select * from flights join passenegrs on flights.id=passengers.flight_id;
db.session.query(flight,passenegrs).filter(flight.id==passenegr.flight_id).all()


"""
