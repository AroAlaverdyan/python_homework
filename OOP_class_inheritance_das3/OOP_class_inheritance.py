# task_1 
# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

import math

class Circle:
	def __init__(self):
		self.radius = self.get_radius()
		
	def get_radius(self):

		check = True
		while check:
			try:
				self.radius = input('\nUser, give me value for radius\n')
				if self.radius.isalpha():
					raise ValueError('Value for radius can only be integer or float type')

				check = False
			except ValueError as v:
				print(v)
		
		print(f"Radius value is:{self.radius}")
		return self.radius

	def Area(self):		
		area = math.pi * (float(self.radius)**2) 

		print("Circle's Area is equal to", area)
		

	def Perimeter(self):
		
		perimeter = 2 * math.pi * float(self.radius)

		print("Circle's Perimeter is equal to", perimeter)

start = Circle()
# print(start.get_radius())
start.Area()
start.Perimeter()

# # task_2 
# # Write a Python class to find a pair of elements(indices of the two numbers)from a given array whose sum equals a specific target number
# print("\n#task_2")
# class Task_2:
	
# 	def __init__(self, list_, target):
# 		self.target = target
# 		self.list_ = list_
	
# 	def Target(self):

# 		circle = 0
# 		print(f"\nList: {self.list_}")
		
# 		for i in self.list_:
# 			for j in self.list_:
				
# 				if circle+1 == len(self.list_):
# 					print("There's no two value, which sum is", self.target)

# 				if circle+1 != len(self.list_) and i + j == self.target:
# 					print(f"\nWhen you sum the {(self.list_[i])+1}th and {(self.list_[j])+1}th numbers of {self.list_},\
#  you will get your target value: {self.target}= {i}+{j}")

# 		circle += 1

# start = Task_2([10, 20, 10, 40, 50, 60, 70], 50)

# start.Target()

# task_3 Create a class named Student, which will inherit the properties and methods from the Person class

# print("\ntask_3")

# class Person:
# 	def __init__(self, course, education_level):
# 		self.course = course
# 		self.education_level = education_level

# class Student(Person):
# 	def __init__(self, sex, age, skin_color, course, education_level):
		
# 		self.sex = sex
# 		self.age = age
# 		self.skin_color = skin_color

# 		Person.__init__(self, course, education_level)
# 		self.course = course
# 		self.education_level = education_level

# start = Student("male", 20, "white", "4th", "A-")

# print(start.__dict__)


# print(start.education_level)