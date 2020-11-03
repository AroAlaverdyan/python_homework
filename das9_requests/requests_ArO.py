import requests

class ImageDownloader:
	def __init__(self, image_list):
		self.image_list = image_list

	def txt_file(self):
		with open("image_list.txt", "w") as f:
			f.write(str(self.image_list))
		return "text file has been created, which is contain list of jpeg and png image's links"

link_list = ["http://httpbin.org/image/jpeg", "http://httpbin.org/image/png"]


class ImageJPG(ImageDownloader):
	def __init__(self, image_list):
		super().__init__(image_list)

	def download(self, i):
		response = requests.get(i)

		with open("image1.jpeg", "wb") as image_jpeg:
			image_jpeg.write(response.content)
				
		return "JPEG image has been downloaded"


class ImagePNG(ImageJPG):
	def __init__(self, image_list):
		ImageDownloader.__init__(self, image_list)

	def download(self, i):
		response = requests.get(i)

		with open("image2.png", "wb") as image_png:
			image_png.write(response.content)

		return "PNG image has been downloaded!!!"

class Result(ImagePNG, ImageJPG):
	def __init__(self, image_list):
		ImageDownloader.__init__(self, image_list)

	def result(self):
		for i in link_list:
			if "jpeg" in i:
				print(ImageJPG.download(self, i))
		
			elif "png" in i:
				print(ImagePNG.download(self, i))


start = Result(link_list)

print(start.txt_file())
start.result()
# 	


#  nuyn xndiri lucumy urish tarberakov

# import requests

# class Jpeg_image:
#     def download(self, link):
#         response = requests.get(link) 
#         with open("image1.jpeg", "wb") as image_png:     
#             image_png.write(response.content)
#         return "jpeg image has been downloaded!!!" 

# class Png_image:
    
#     def download(self, link):
#         response = requests.get(link) 
#         with open("image2.png", "wb") as image_png:     
#             image_png.write(response.content)
#         return "PNG image has been downloaded!!!" 

# class ImageDownloader(Png_image,Jpeg_image):
#     def __init__(self, list_image):
#         self.list_image = list_image
    
#     def download(self):
#         for link in self.list_image:
#             if link.endswith("png"):
#                 text = Png_image.download(self, link)

#             elif link.endswith("jpeg"):
#                 text = Jpeg_image.download(self, link)

#             else:
#                 print("wrong type")
#             print(text)

# link_list = ["http://httpbin.org/image/jpeg", "http://httpbin.org/image/png"]
# obj = ImageDownloader(link_list)
# obj.download()




# առաջին տարբերակի ավելի ճիշտ տարբերակ, բայց սխալները ուղղված չեն, ժառանգելու պահն ա ճիշտ արած

# import requests
# link_list = ["http://httpbin.org/image/jpeg", "http://httpbin.org/image/png"]
# class ImageJPG():
#     def download(self):
#         response = requests.get(i)
#         with open("image1.jpeg", "wb") as image_jpeg:
#             image_jpeg.write(response.content)
#         return "JPEG image has been downloaded"
# class ImagePNG:
#     def download(self):
#         response = requests.get(i)
#         with open("image2.png", "wb") as image_png:
#             image_png.write(response.content)
#         return "PNG image has been downloaded!!!"
# class ImageDownloader(ImageJPG,ImagePNG):
#     def __init__(self, image_list):
#         self.image_list = image_list
#     def txt_file(self):
#         with open("image_list.txt", "w") as f:
#             f.write(str(self.image_list))
#         return "text file has been created, which is contain list of jpeg and png image's links"
# class Result(ImageDownloader):
#     def __init__(self, image_list):
#         ImageDownloader.__init__(self, image_list)
#     def result(self):
#         for i in link_list:
#             if "jpeg" in i:
#                 print(ImageJPG.download(self))
#             elif "png" in i:
#                 print(ImagePNG.download(self))
# start = Result(link_list)
# print(start.txt_file())
# start.result()