
import threading
import time
import datetime
import concurrent.futures

def function_1():
	for i in range(10):
		time.sleep(0.5)
		print(i)

# # how to detect which is the main running file
if __name__ == '__main__':
	starting_time = datetime.datetime.today()

	# # running code without threads
	# for i in range(4):
	# 	function_1()

	# b = (datetime.datetime.today() - starting_time).seconds

	# print(f"it took {b} seconds")


	# using threads to run code more efficiently
	# thread_list = []
	# for i in range(4):
	# 	x = threading.Thread(target = function_1)
	# 	thread_list.append(x)
	# 	x.start()

	# b = (datetime.datetime.today() - starting_time).seconds
	# print(f"it took {b} seconds")

	# using thread.join function to make main thread wait for the others:
	thread_list = []
	for _ in range(4):
		x = threading.Thread(target = function_1)
		thread_list.append(x)
		x.start()

	for thread in thread_list:
		thread.join()
	b = (datetime.datetime.today() - starting_time).seconds
	print(f"it took {b} seconds")

	# passing arguments to a thread function and deamon treads
	# def function_1(range_num):

	# 	for i in range(range_num):
	# 		time.sleep(0.5)
	# 		print(i)

	# thread_list = []
	# for _ in range(4):
	# 	x = threading.Thread(target = function_1, args = (5,), daemon = True)
	# 	thread_list.append(x)
	# 	x.start()

	# for thread in thread_list:
	# 	thread.join()
	# b = (datetime.datetime.today() - starting_time).seconds
	# print(f"it took {b} seconds")
	

	# version II
				   # (10, "a")
	# def function_1(range_num):

	# 	for i in range(range_num[0]):
	# 		time.sleep(0.5)
	# 		print(range_num[1], i)

	# with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
	# 	executor.map(function_1, [(10, "a"), (10, "b"), (10, "c"), (10, "d")]) 

	# b = (datetime.datetime.today() - starting_time).seconds
	# print(f"it took {b} seconds")

	# import multiprocessing

	# h = []  
	# for i in range(2):
	# 	c = multiprocessing.Process(target = function_1)
	# 	h.append(c)
	# 	c.start()

	# for i in h:
	# 	i.join()
	# b = (datetime.datetime.today() - starting_time).seconds
	# print(f"it took {b} seconds")