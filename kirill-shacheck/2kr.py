# Вариант 8


# 1.

class Item:
	def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Warehouse:
	def __init__(self):
		self.item = Item(«Ноутбук», 0)

	def add_item(self, amount):
		self.item.quantity += amount
		print(«Товар добавлен на склад»)

warehouse = Warehouse()

warehouse.add_item(5)

print("Товар:", warehouse.item.name)

print("Количество:", warehouse.item.quantity)


# 2.

class Machine:
	def __init__(self, capacity, model):
		self.__capacity = capacity
		self._model = model 

	def display_info():
		print(«Модель:», self._model)

	def calculate_load(self):
		return self.__capacity

	def calculate_energy(self):
   		return self.__capacity * 2

class Washer(Machine):
	def calculate_load(self):
		return super().calculate.load * 2

	def calculate_energy(self):
		return super().calculate_energy() * 2

class Dryer(Machine):
	def calculate_load(self):
		return super().calculate.load * 3

	def calculate_energy(self):
		return super().calculate.energy * 5

class LaundryMachine(Washer, Dryer):
		pass

machine = LaundryMachine(5, «LG»)

machine.display_info()

print("Загрузка Washer:", Washer.calculate_load(machine))
print("Загрузка Dryer:", Dryer.calculate_load(machine))

print("Энергия Washer:", Washer.calculate_energy(machine))
print("Энергия Dryer:", Dryer.calculate_energy(machine))

print("Загрузка LaundryMachine:", machine.calculate_load())
print("Энергия LaundryMachine:", machine.calculate_energy())






				