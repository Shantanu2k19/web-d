/* 
version used : postgresql
sql used to interact with data mainly tabular
to start postgresql : 
$ sudo su postgres
$ psql
*/
CREATE TABLE flights(
	id SERIAL PRIMARY KEY,
	origin VARCHAR NOT NULL,
	destination VARCHAR NOT NULL,
	duration INTEGER NOT NULL);

INSERT INTO flights
	(origin,destination,duration)
	VALUES('delhi','mysore',120);

INSERT INTO flights
	(origin,destination,duration)
	VALUES('delhi','mumbai',100);

--to view whole table -> 
SELECT * FROM flights;

--for specific column: replace * with column name 
--for specific row :SELECT * FROM flights WHERE id=2 AND duration<50 AND destination='lol';
--semicolon important for displaying table

SELECT AVG(duration) FROM flights ; --WHERE..

--number of rows: 
SELECT COUNT(*) FROM flights; --where....

--can also use max,avg,sum,count 
select MIN(duration) from flights; 
	
--where origin is delhi or goa
select * from flights where origin in ('delhi','lol');

--occurence of text b/w placeholders(%), even if its a substing
--following will return all where origin contain 'o' in it
select * from flights where destination like '%o%';

--\d : show relations\variables


UPDATE flights
set duration=430 where origin ='delhi' and destination='mysore';

delete from flights where destination = 'mumbai';

--for viewing only 2 rows of the entire table
select * from flights limit 2;

--sorting list
select * from flights order by duration asc; --asc:ascending , desc: desending 

--3 shortest flights 
select * from flights order by duration asc limit 3;


--count no of same origins and shows it 
select origin,count(*) from flights group by origins;
	
--origins more than 1
select origin, count(*) from flights group by origin having count(*)>1;



--TABLE PASSANGERS
create table passengers(
	id serial primary key,
	name varchar not null,
	flight_id integer references flights --referencing to id's of flights table, its for constrain, not connecting tables actually
);
insert into passengers (name,flight_id) values ('shan',1);
--mandy, momo inserted


--JOIN is used to access data from both tables 
--joining two table to access relatable data using:
select origin,destination,name from flights join passengers on passengers.flight_id=flights.id; --flight_id == id
--this join all the matched pairs, inner joint

--will join even the unmatched pair too, include all data from LEFT(flights) 
select origin,destination,name from flights LEFT join passengers on passengers.flight_id=flights.id; 

--right joint, include all data from right(passengers) 
select origin,destination,name from flights right join passengers on passengers.flight_id=flights.id; 

--to view passenger details 
select origin,destination,name from flights join passengers on passengers.flight_id=flights.id where name='momo';
---2 commands to do this from seperate tables, now just one command from a single joined table;


--nested querry 
select flight_is from passengers group by flight_id having count(*)>1;
--or nested querry 
select * from flights where id in (select flight_id from passengers group by flight_id having count(*)>1);  

--1' OR '1'='1'  password hack for simple sql user-pass code
