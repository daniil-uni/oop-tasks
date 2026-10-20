class Product:
	def __init__(self, name_product, sale):
		self.name_product = name_product
		self.sale = sale
	
class Shop(Product):
	def __init__(self, name_shop):
		self.name_shop = name_shop
	
	store = {}

	def accept_order(self, product):
		self. store[product.name] = product.sale
		print(/f"Стоимость {name_product} - {sale}
		




class MediaFile: 
	def __init__(self, duration, name):
		self.__duration = duration
		self._name = name

	def get_duration(self):
		return duration

	def get_name(self):
		return name

	def display_info(self):
		print(/f"Длительность: {__duration}, название: {_name}")

class Audio(MediaFile):
	def __init__(self, duration, name, size):
		self.size = size
		super.__init__(self, duration, name)

	def calculate_size(self):
		self.size = duration * 5

	def play(self):
		self.__duration = duration * 5

	def display_info(self):
		print(/f"Длительность: {__duration}, название: {_name}", размер: {size})


class Video(MediaFile):
	def __init__(self, duration, name, size):
		self.size = size
		super.__init__(self, duration, name)

	def calculate_size(self):
		self.size = duration * 20

	def play(self):
		self.__duration = duration / 2

	def display_info(self):
		print(/f"Длительность: {__duration}, название: {_name}", размер: {size})

class Multimedia(Audio, Video):
	...

Multimedia.Audio.play()



	


		