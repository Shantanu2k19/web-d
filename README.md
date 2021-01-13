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



6. SQL_PYTHON : python equivalent codes and application of sql 
      airline2- all the template code are same
           the application.py file and models.py files are changed, python equivalent of sql code from airline1 is used

      create_table: make class(template) for tables(flight,passengers), 
          then create table, 
          insert data from csv file, 
          manipulate and prints it in list.py(also include python equivalent code for sql)

      classes.py is an exapmle  for classes in python, 
      currency.py is exapmle for api, requests and status_code
      json.py is python file to print json data from api link of a website using python


7. JAVASCRIPT : 
      1) hello.html :querySelector: searchinf for certain tag to update, a counter to increment value and alert at multiples of 10, alerts for different actions.
      2) counter (contains counter.html calling counterjava.js) : examle to show calling of js file from html
      3) formAlert.html :takes name of user, alerts with hello {name}
      4) interval.html :update counter on screen after every 1000ms, exaple to use time in website
      5) tasks.html :make unordered list of task, does not allow user to make empty task, use of addEventListener
      6) button_color.html :change the color of text on screen based on selected button or drop down list, arrow notation function also shown.
      7) storage.html :example to use local STORAGE, updates counter and stores value even after reload
      8) ajax: Asynchronous JavaScript and XML 
             currency : uses api link to take currency from user, and give exchange rate 
             vote0 : shows the voted option on all screens of website(broadcasting), hands on backend python, js and html based flask application 
             vote1 : shows the total number of votes for the options, updates synchronously for all the users   



DJANGO : LECTURE & 
django-admin startproject mysite
creates mysite name project with files : 
manage.py  : python script to perform operations on website
mysite folder : 
asgi.py
  __init__.py : tells mysite directory is a python package
  settings.py : setting for web app, time zone, database etc.
  urls.py : file to take care of url and routes user of website can go to 
  wsgi.py : way to host website, kinda


to create an app : python manage.py startapp name
do some shit
running webapp : 
directory : mysite
command : python manage.py runserver



php : installed in wndows: 1. extracted the file in C\:Users\shant\php
- added route to php from start-environment-environment variables-paths-edit path- added path to php
    : created a folder www at Users\shant\www
    and created a file site.php in it
    : for starting server, in cmd: php -S localhost:4000
    : go to url http://localhost:4000/www/site.php for website 
1. added string basics and basic php file

site 2: checkboxes , arrays 
site 3:  functions, associated arrays(pairs)
site 4: if, switch, while, for loop
site 5: to add html and other php files to website using "include", footer.html and header.php used in this file
