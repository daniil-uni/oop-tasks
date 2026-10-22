class Product:
    def __init__(self, name_product, sale):
        self.name_product = name_product
        self.sale = sale


class Shop:
    def __init__(self, name_shop):
        self.name_shop = name_shop
        self.store = {}

    def accept_order(self, product):
        self.store[product.name_product] = product.sale
        print(
            f"Магазин: {self.name_shop}. "
            f"Стоимость {product.name_product} — {product.sale}"
        )


product = Product("Ноутбук", 250000)
shop = Shop("Магазин техники")
shop.accept_order(product)



class MediaFile: 
	def __init__(self, duration, name):
		self.__duration = duration
		self._name = name

	def get_duration(self):
		return self.__duration

	def set_duration(self, duration):
		self.__duration = duration

	def get_name(self):
		return self._name

	def display_info(self):
		print(f"Длительность: {self.__duration}, название: {self._name}")

class Audio(MediaFile):
	def __init__(self, duration, name, size=0):
		super().__init__(duration, name)
		self.size = size

	def calculate_size(self):
		self.size = self.get_duration() * 5
		return self.size

	def play(self):
		self.set_duration(self.get_duration() * 5) 
		print(f"Аудио {self.get_name()}, длительность: {self.get_duration()}")

	def display_info(self):
		print(f"Длительность: {self.__duration}, название: {self._name}, размер: {self.size}")


class Video(MediaFile):
	def __init__(self, duration, name, size):
		super.__init__(duration, name)
		self.size = size


	def calculate_size(self):
		self.size = self.get_duration() * 20
		return self.size
	
	def play(self):
		self.set_duration(self.get_duration() / 2) 
		print(f"Аудио {self.get_name()}, длительность: {self.get_duration()}")

	def display_info(self):
		print(f"Длительность: {self.__duration}, название: {self._name}, размер: {self.size}")


class Multimedia(Audio, Video):
    pass


media = Multimedia(120, "Песня", 0)
media.play()