my_dict = {'1':['a','b'], '2':['c', 'd'], '3':['x', 'y']}

new_list = []
for i in my_dict.keys():
	new_list += i

circle_for_1 = 0

for value_1 in my_dict[new_list[circle_for_1]]:
	circle_for_1 += 1
	for value_2 in my_dict[new_list[1]]:
		for value_3 in my_dict[new_list[2]]:
			print(value_1 + value_2 + value_3)

print("Aro")


