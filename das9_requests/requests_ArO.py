import requests

class ImageDownloader:
	def __init__(self, image_list):
		self.image_list = image_list

	def txt_file(self):
		with open("image_list.txt", "w") as f:
			f.write(str(self.image_list))
		return "text file has been created, which is contain list of jpeg and png image's links"


class ImageJPG(ImageDownloader):
	def __init__(self, image_list):
		super().__init__(image_list)

	def download(self):
		response = requests.get(self.image_list[0])

		with open("image1.jpeg", "wb") as image_jpeg:
			image_jpeg.write(response.content)
		
		return "JPEG image has been downloaded"


class ImagePNG(ImageJPG):
	def __init__(self, image_list):
		ImageDownloader.__init__(self, image_list)

	def download(self):
		response = requests.get(self.image_list[1])

		with open("image2.png", "wb") as image_png:
			image_png.write(response.content)

		return "PNG image has been downloaded!!!"

class Result(ImagePNG):
	def __init__(self, image_list):
		ImageDownloader.__init__(self, image_list)

	def result(self):
		return f'{ImageJPG.download(self)},	\n{ImagePNG.download(self)}'

link_list = ["http://httpbin.org/image/jpeg", "http://httpbin.org/image/png"]


start = Result(link_list)

print(start.txt_file())
print(start.result())
