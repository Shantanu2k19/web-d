import os
import csv
#csv is a comma seperated file, 

#sqlalchemy library used
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#                                 (username)(pass)  (host)  |(name of database where data is stored)
engine = create_engine("postgresql://zodiac_sql:shan@localhost/postgres") #os.getenv("DATABASE_URL"))
#engine is managing the connection with database, created using lib sqlalchemy
#database_url is the environment variable, url of database, in this case of local host

db = scoped_session(sessionmaker(bind=engine))

def main():

	#inserting data froma csv file, data gets added everytime you run the file 
	f = open("flights.csv")
	reader = csv.reader(f)  #read file f as csv file
	for origin, destination, duration in reader:
		db.execute("insert into flights (origin, destination, duration) values (:origin, :destination, :duration)",{"origin": origin, "destination": destination, "duration":duration})
		print(f"added flight from: {origin} to {destination} lasting : {duration}mins")
	db.commit()
	

	print("\n")  #new line

    #fetching all data to read and print
	flights=db.execute("SELECT origin,destination,duration FROM flights").fetchall()
	#select all data from flights table
	for flight in flights:
		print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")
    

if __name__ == "__main__":
	main()
