# web-d
1. basic html and css, gun.png file for links.html
2. flask_app : basic : application.py :: export FLASK_APP=application.py
                      other files in template folders, flask run
3. forms using flask
4. notes:: take data from user, display in form of notes, use sessions for different notes for different user

5. SQL
basic : basic sql commands to manipulate flights table, created using basic.sql
database created : name: postgres
username : zodiac
password : elonmusk

DATABASE  : FLIGHTS
postgres=# select * from flights;
 id | origin | destination | duration 
----+--------+-------------+----------
  3 | goa    | assam       |      530
  4 | up     | bihar       |       40
  5 | delhi  | kolkata     |      180
  6 | york   | hp          |       30
  1 | york   | mysore      |      430
 26 | paris  | new york    |      374
 27 | tokyo  | shanghai    |      355
 28 | mexico | bangalore   |      321
(8 rows)

PASSENGERS :
postgres=# select * from passengers;
 id | name  | flight_id 
----+-------+-----------
  1 | shan  |         1
  2 | mandy |         3
  3 | momo  |         5
  4 | lol   |         3
  5 | lol   |         3
  6 | kahe  |         5
  7 |       |         6
  8 | haha  |         3
(8 rows)


now, to add flights using python, use LIST.py (adds flights from .csv file)
to view, use PASSENGERS.py (view flight details as well as passengers after entering flight id)
actions performed using python, above can also be done using SQL in postgres

now, application: AIRLINE
file 1: {application.py}   : main file, perform following operations respectively
route 1: book flight (INDEX.html)(LAYOUT.html)
          drop down menu for selecting flights, take name as input, button to book flight

route 2: after getting name and flight from user above, redirected to this route\check if name empty
        (ERROR.html)
        make sure flight exist
        (SUCCESS.html)

route 3: view list of flights
          (FLIGHTS.html) view flights

route 4: view passengers on certain flight
          (FLIGHT.html) list flight detail, all passengers travelling
