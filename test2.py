# 5 Вариант
class Product:
	def __init__ (self, contain, name, price):
		self.contain = contain
		self.name = name
		self.price = price
	def info_product (self):
		return contain, name, price
class Shop:
	def __init__ (self, name):
		self.name = name
	def accept_order (self, product):
		print( "В магазине: ", name, "есть такой товар\n", product.info_product())
product = Product("Нужно хранить в холоде", "Мясо", 1000)
shop = Shop("Магнум")
shop.accept_order(product)
	