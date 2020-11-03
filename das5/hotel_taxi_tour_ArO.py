class Hotel:
	def __init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price, discount_1):
		self.name = name
		self.place = place
		self.rooms_mid = rooms_mid
		self.mid_room_price = mid_room_price
		self.rooms_lux = rooms_lux
		self.lux_room_price = lux_room_price
		self.discount_1 = discount_1

	def presentation(self):
		text = f"We will stay at {self.name} hotel which is located near the {self.place}. We offer 2 types of rooms:\
middle - {self.mid_room_price}AMD and lux - {self.lux_room_price}AMD"
		return text

	def booking(self):
		check = True
		while check:
			try:
				room_booking_input = input("\nOkay, let's choose which type of room do you want - 1/for mid, 2/for lux\n")
				if room_booking_input != "1" and room_booking_input != "2":
					raise ValueError("Please, give correct value)))")
				
				check = False			
			except ValueError as v:
				print(v)
		
		if room_booking_input == "1":
			print(f"That type of room price is {self.mid_room_price}")
			check = True
			while check:
				try:
					mid_input = input("\nNow book a room which is free(room1/room2/room3)\n")
					if mid_input != "room1" and mid_input != "room2" and mid_input != "room3":
						raise NameError('Please give me correct value')
	
					if self.rooms_mid[mid_input] == "busy":
						raise KeyError("That room is BUSY")

					check = False
				except NameError as n:
					print(n)
				except KeyError as k:
					print(k)
			
			self.rooms_mid[mid_input] = "busy"
			print("After your book we have the following schedule of the mid_rooms:", self.rooms_mid)
		
		elif room_booking_input == "2":
			print(f'That type of room price is {self.lux_room_price}')
			check = True
			while check:
				try:
					lux_input = input("\nNow book a room which is free(room1/room2/room3)\n")
					if lux_input != "room1" and lux_input != "room2" and lux_input != "room3":
						raise NameError('Please give me correct value')
					
					if self.rooms_lux[lux_input] == "busy":
						raise KeyError("Sorry, that room is BUSY")
					
					check = False
				except NameError as n:
					print(n)
				except KeyError as k:
					print(k)

			self.rooms_lux[lux_input] = "busy"
			print("After your book we have the following schedule of the lux_rooms:", self.rooms_lux)

	def available_room_check(self):
		check = True
		while check:
			try:
				room_booking_input = input("\n!!!!!Choose which type of room do you want - 1/for mid, 2/for lux\n")
				if room_booking_input != "1" and room_booking_input != "2":
					raise ValueError("Please, give correct value)))")
				
				check = False			
			except ValueError as v:
				print(v)
		
		if room_booking_input == "1":
			free_rooms_list = []
			for i in self.rooms_mid:
				
				if self.rooms_mid[i] == "free":
					free_rooms_list.append(i)
				
			if len(free_rooms_list) != 0:
				print(f'Free rooms list is:{free_rooms_list}')
			else:
				print("Sorry, we don't have free rooms((")
		
		elif room_booking_input == "2":
			free_rooms_list = []
			for i in self.rooms_lux:
				if self.rooms_lux[i] == "free":
					free_rooms_list.append(i)

			if len(free_rooms_list) != 0:
				print(f"Free rooms list is {free_rooms_list}")
			else:
				print("Sorry, but we don't have free lux rooms, all rooms are busy.")
		self.a = room_booking_input

	def price_discount(self):
		self.available_room_check()
			
		if self.a == "1":
			a = (self.mid_room_price * self.discount_1)/100
			self.mid_room_price -= a
			return f' New price for mid_rooms: {self.mid_room_price}AMD'
			
		elif self.a == "2":
			b = (self.lux_room_price * self.discount_1)/100
			self.lux_room_price -= b
			return f'New price for lux_rooms: {self.lux_room_price}AMD'

start = Hotel("Bass", "Aygestan", {"room1": "free", "room2": "busy", "room3": "free"}, 10000, {"room1": "busy", "room2": "free", "room3": "busy"}, 20000, 10)

start.booking()
start.available_room_check()
print(start.price_discount())


class Taxi:
	def __init__(self, taxi_name, car_types, price_for_tour, discount_2):
		self.taxi_name = taxi_name
		self.car_types = car_types
		self.price_for_tour = price_for_tour
		self.discount_2 = discount_2

	def presentation(self):
		text = f'Transport with {self.taxi_name} company, which provides {self.car_types} cars and price for it is {self.price_for_tour}'
		return text

	def price_discount(self):
		print("Old price for tour is", self.price_for_tour,"AMD")
		c = int(self.price_for_tour * self.discount_2)/100
		self.price_for_tour -= c
		return f"Discounted price for car is {int(self.price_for_tour)}AMD, {self.discount_2}% discount"

mercedes = Taxi("Ride over", "mercedes", 10000, 10)
print("\n#taxi class")
print(mercedes.price_discount())


class Tour(Hotel, Taxi):
	def __init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price, discount_1, taxi_name, car_types, price_for_tour, discount_2, tour_name, price_lux, price_mid):
		Hotel.__init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price, discount_1)
		Taxi.__init__(self, taxi_name, car_types, price_for_tour, discount_2)
		self.tour_name = tour_name
		self.price_lux = price_lux
		self.price_mid = price_mid

	def global_presentation(self):
		print(f'\nHello we offer {self.tour_name}, we have two options: {self.price_lux} and {self.price_mid} which includes', Taxi.presentation(self), Hotel.presentation(self))
		


Aro_tour = Tour("Lerane", "Geghard", {"room1": "free", "room2": "busy", "room3": "free"}, 20000, {"room1": "busy", "room2": "free", "room3": "busy"}, 40000, 10, "Ride over\
", "Mercedes", 10000, 10, "Geghard tour", 50000, 30000)

Aro_tour.global_presentation()