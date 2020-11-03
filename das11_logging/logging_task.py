import logging
import random

def num_dicider():

	any_number = random.randint(0, 50)
	print(any_number)
	logging.basicConfig(filename = "number_errors.log", filemode = "w", format = "%(asctime)s -- %(levelname)s -- %(message)s", level = logging.DEBUG)

	if any_number >= 0 and any_number <= 9:
		logging.debug(f"Number is {any_number}")
						
	elif any_number >= 10 and any_number <= 19:
		logging.info("Program is normaly working")		

	elif any_number >= 20 and any_number <= 29:
		logging.warning("The number is approximately to half of the max value.")			

	elif any_number >= 30 and any_number <= 39:
		logging.error("The number is getting closer to the max value.")		

	elif any_number >= 40 and any_number <= 50:
		logging.critical(f"Be carefull. Number({any_number}) is more closer to the max valu than before.")


for _ in range(3):
	
	num_dicider()
		






