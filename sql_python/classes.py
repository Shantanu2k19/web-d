#classes in python

class flight:

	counter = 1

	def __init__(self, origin, destination, duration):

		#keep track of id number
		self.id = flight.counter
		flight.counter += 1

		self.origin = origin
		self.destination = destination
		self.duration = duration

	def print_info(self):
		print(f"flight origin : {self.origin}")
		print(f"flight destination : {self.destination}")
		print(f"flight duration : {self.duration}")

		print("\nPassengers :")
		for passengers in self.passengers:
			print(f"{passengers.name}")

	def delay(self, amount):
		self.duration += amount

		#keep track of passengers
		self.passengers = []

	def add_passenger(self, p):
		self.passengers.append(p)
		p.flight_id = self.id


class passengers:

	def __init__(self, name):
		self.name = name

def main():

	#creating flight object
	f1 = flight(origin = "delhi", destination="arizona", duration=500)
	f1.duration -= 300

	f1.delay(200)

	#cadd passengers
	shan = passengers(name = "shan")
	pdf  = passengers(name = "pdf")

	#add passengers
	f1.add_passenger(shan)
	f1.add_passenger(pdf)
	f1.print_info()

if __name__ == "__main__":
	main()
