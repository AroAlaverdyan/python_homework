import time
import datetime
import json
import threading
import requests

class ImageDown():
	def __init__(self):
		dict_jpg = {}
		dict_png = {}
		
		self.dict_jpg = dict_jpg
		self.dict_png = dict_png

		with open("2homework8.json", "r") as f:
			file = json.load(f)

			for i in range(len(file["items"])):

				name = file["items"][i]["name"]
				url = file["items"][i]["url"]
					
				if url.endswith("jpg"):
					self.dict_jpg.setdefault(name, url)
						

				elif url.endswith("png"):
					self.dict_png.setdefault(name, url)
	
	def Result(self):				

		def jpg_photo(key_as_name):
			response = requests.get(self.dict_jpg[key_as_name])

			with open(f"{key_as_name}.jpeg", "wb") as image:
				image.write(response.content)

			print(f"{key_as_name}.jpeg has been successfuly downloaded")

		def png_photo(key_as_name):
			response = requests.get(self.dict_png[key_as_name])

			with open(f"{key_as_name}.png", "wb") as image:
				image.write(response.content)

			print(f"{key_as_name}.png has been successfuly downloaded")


		if __name__ == "__main__":
			starting_time = datetime.datetime.today()
			thread_list = []
			for i in self.dict_jpg:
				x = threading.Thread(target = jpg_photo, args = (i,))
				thread_list.append(x)
				x.start()
			for j in self.dict_png:
				x = threading.Thread(target = png_photo, args = (j,))
				thread_list.append(x)
				x.start()
			
			for thread in thread_list:
				thread.join()
			b = (datetime.datetime.today() - starting_time).seconds
			print(f"it took {b} seconds")

start = ImageDown()
start.Result()