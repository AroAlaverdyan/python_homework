import random
from collections import Counter

class Dict:
	def __init__(self, my_string):
		self.my_string = my_string

	def task_1(self):
		my_dict = {}
		
		for i in String.my_string:
			value = random.randint(0,9)
			my_dict.update({i: value})
		print("#task_1",'\nNew dictionary is:', my_dict) 

	def task_2(self):
		my_dict = {}
		deleted_dict = {}
		deleted_items = 0
		for i in String.my_string:
			value = random.randint(0,9)
			
			if not value in my_dict.values():
				my_dict.update({i: value})
			else:
				deleted_items += 1
				deleted_dict.update({i: value})
		print("\n#task_2",'\nNew dictionary without duplicate values', my_dict)
		if deleted_items != 0:
			print('Deleted items is:', deleted_items,'and it is:', deleted_dict)
		else:
			print('Deleted items is:', deleted_items)


	def task_3(self):
		new_dict = {}
		mmax = []
		
		for i in String.my_string:
			value = random.randint(0,9)
			new_dict.setdefault(i, value)
		keys_number = len(new_dict)
		mecic_poqr = Counter(new_dict)
		max_3 = mecic_poqr.most_common(keys_number)

		print("\n#task_3",'\nDictionary:', new_dict)
		print('Three maximum values:')

		for i in max_3:
			if len(mmax) < 3:
				if not i[1] in mmax:
					mmax.append(i[1])
					print(i[1])
			
String = Dict('python')

String.task_1()
String.task_2()
String.task_3()
