# import random
# class HouseHeating:
# 	def __init__(self, goal_temp_cold, goal_temp_hot, house):
# 		self.__goal_temp_cold = goal_temp_cold
# 		self.__goal_temp_hot = goal_temp_hot
# 		self.__house = house
# 		self.season = self.get_all()

# 	def get_all(self):
# 		check = True
# 		while check:
# 			try:
# 				self.season = input("\nUser, say what season is: cold or hot\n")

# 				if self.season != "cold" and self.season != "hot":
# 					raise ValueError(f"{self.season} is not right value, read what I want!!!")
# 				check = False
# 			except ValueError as v:
# 				print(v)

# 		if self.season == "cold":
# 			for i in self.__house:			
# 				if self.__house[i] < (self.__goal_temp_cold-5):
# 					print(f"{i}'s current temperature is {self.__house[i]}°C, but it is so low, you should raise minimum {self.__goal_temp_cold - self.__house[i]}°C")
					
# 				elif (self.__goal_temp_cold-4) < self.__house[i] < (self.__goal_temp_cold+13) :
# 					print(f"{i}'s temperature:{self.__house[i]}°C is normal")
# 				else:
# 					print(f"{i}'s temperature is {self.__house[i]}°C and it is too hot")
					
# 		elif self.season == "hot":
# 			for i in self.__house:
# 				if self.__house[i] > (self.__goal_temp_hot+10):
# 					print(f"{i}'s temp is {self.__house[i]}°C and it is too hot, you'll feel bad. Turn on condition to dicrease the temperature to {self.__goal_temp_hot}°C")
					
# 				elif (self.__goal_temp_hot-5) < self.__house[i] <= (self.__goal_temp_hot+10):
# 					print(F"{i}'s temperature is {self.__house[i]}°C and it is normal for {self.season} weather.")
# 				else:
# 					print(f"{i}'s temperature is {self.__house[i]}°C and it is too cold")
# 		return self.season
	
# 	def set_all(self, new_house):
# 		self.__house = new_house
# 		print("\nNow with changed house values\n")
# 		print(new_house, "\n")
# 		if self.season == "cold":
# 			for i in new_house:			
# 				if new_house[i] < self.__goal_temp_cold:
# 					print(f"{i}'s current temperature is {new_house[i]}°C, but it is so low")
# 					new_house[i] = random.randint((self.__goal_temp_cold), (self.__goal_temp_cold+5))
# 					print(f"I'll set the right temperature for {self.season} season. And now {i}'s temp is {new_house[i]}")
# 				else:
# 					print(f"{i} temperature is {new_house[i]} and it is normal for {self.season} weather")

# 		elif self.season == "hot":
# 			for i in new_house:
				
# 				if new_house[i] > self.__goal_temp_hot:
# 					print(f"{i}'s temp is {new_house[i]}°C and it is too much")
# 					new_house[i] = random.randint((self.__goal_temp_hot-5), (self.__goal_temp_hot))
# 					print(f"I'll set the right temperature for {self.season} season. And now {i}'s temp is {new_house[i]}")
# 				else:
# 					print(f"{i} temperature is {new_house[i]} and it is normal for {self.season} weather")

# Home1 = HouseHeating(30, 17, {"room1": 29, "room2": 40, "room3": 10, "room4": 0})
# # Home1.get_all()
# Home1.set_all({"room1": 13, "room2": 25, "room3": -5, "room4": 38})




class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person name is {self.name}'

	def __str__(self):
		return F"Hello {self.name}"

	def __eq__(self, other):
		if self.age == self.other:
			return True
		else:
			return False

Aro = Person("Aro", 20)

print(Aro, 19)







