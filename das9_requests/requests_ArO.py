import requests

class ImageDownloader:
	def __init__(self, image_list):
		self.image_list = image_list

	def txt_file(self):
		with open("image_list.txt", "w") as f:
			f.write(str(self.image_list))
		return "text file has been created, which is contain list of jpeg and png image's links"

link_list = ["http://httpbin.org/image/jpeg", "http://httpbin.org/image/png"]

for i in link_list:
	if "jpeg" in i:

		class ImageJPG(ImageDownloader):
			def __init__(self, image_list):
				super().__init__(image_list)

			def download(self):
				response = requests.get(i)

				with open("image1.jpeg", "wb") as image_jpeg:
					image_jpeg.write(response.content)
				
				return "JPEG image has been downloaded"

	elif "png" in i:
		class ImagePNG(ImageJPG):
			def __init__(self, image_list):
				ImageDownloader.__init__(self, image_list)

			def download(self):
				response = requests.get(i)

				with open("image2.png", "wb") as image_png:
					image_png.write(response.content)

				return "PNG image has been downloaded!!!"

class Result(ImagePNG):
	def __init__(self, image_list):
		ImageDownloader.__init__(self, image_list)

	def result(self):
		print(ImageJPG.download(self))
		print(ImagePNG.download(self))


start = Result(link_list)

print(start.txt_file())
start.result()
