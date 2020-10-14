class Country:
	def __init__(self, continent, country_name):
		self.continent = continent
		self.country_name = country_name
		
	def presentation_for_country(self):
		text_for_country = f'It has been produced in {self.continent}, more specifically in {self.country_name}'
		return text_for_country

class Brand:
	def __init__(self, brand_name, business_start_date):
		self.brand_name = brand_name
		self.business_start_date = business_start_date

	def presentation_for_brand(self):
		text_for_brand = f"You can buy it from {self.brand_name}, which has started its business in {self.business_start_date}"
		return text_for_brand

class About_brand:
	def __init__(self, owner, source_of_inspiration):
		self.owner = owner
		self.source_of_inspiration = source_of_inspiration

	def presentation_for_season(self):
		text_for_season = F"The founder of the brand is {self.owner}. Her source inspiration is her videoclip which name is {self.source_of_inspiration}."
		return text_for_season

class Product(Country, Brand, About_brand):
	def __init__(self, product_name, type_, price, quantity, continent, country_name, brand_name, business_start_date, owner, source_of_inspiration):
		self.product_name = product_name
		self.type_ = type_
		self.price = price
		self.quantity = quantity
		self.discount = 10

		Country.__init__(self, continent, country_name)
		Brand.__init__(self, brand_name, business_start_date)
		About_brand.__init__(self, owner, source_of_inspiration)

	def presentation_1(self):
		print(f"\nToday we're presenting our new {self.product_name}\n")
		print(self.presentation_for_country())
		print(self.presentation_for_brand())
		print(self.presentation_for_season())
		print(f'\nNow more details about {self.product_name}: \nType: {self.type_} \nPrice: {self.price}$ \nQuantity: limited edition - {self.quantity} pcs')

	def presentation_discount(self):
		a = (self.price * self.discount)/100
		new_price = int(self.price - a)
		print(f"\nWe have special offer for you. If you buy our {self.product_name} today, you'll get {self.discount}% off. So it'll be cost {new_price}$")

	def presentation_quantity(self):
		new_quantity = self.quantity + 50
		text_for_quantity = F"\nIf the buyers be a lot, we will increase {self.product_name} quantity, making {new_quantity} pcs"
		return text_for_quantity

ring = Product(" Ring 'Dove'", 'silver', 67, 100, 'Asia', 'Armenia', 'Pregomesh', "2013", 'SIRUSHO', 'PreGomesh')

ring.presentation_1()
ring.presentation_discount()
print(ring.presentation_quantity())