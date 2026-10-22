Задание 1 
10 ВАРИАНТ

Class component:
	def__init__(self, name, cost):
		self.name = name
		self.name = cost

	def add_component(self, component):
		print("Компонент добавлен", component.name)

Class computerSystem:
	def def__init__(self, name):
		self.name = name
		self.components = []
	
	def add_component(self, component):
		self.components.append(component)

	def show_info(self):
		print("Компьютер", self.name)
	for component.name in self component:
		print(component.name, "-", component.cost, "tr")

cpu = component("процессор", 50000)
ram = component("оперативаня память", 2500000)
disk = component("SSD", 30000)

computer = ComputerSystem("PC")
computer.add_component(cpu)
computer.add_component(ram)
computer.add_component(disk)

computer.show_info()

Задание 2 
Вариант 10

class Animal:
	def __init__(self,age):
		self.__age = age
	
	def get_age(self):
		return self.__age

	def display_info(self):
	print("Возраст:", self.__age)

class Bird(Animal):
	def calculate_speed(self):
		return self.get_age() * 6 
	
	def calculate_energy(self):
		return self.get_age() * 3

class Fish(Animal):
	def calculate_speed(self):
		return self.get_age() * 2
	
	def calculate_energy(self):
		return self.get_age() * 4

bird = Bird(4)
fish = Fish(6)

print("Птица:")
bird.display_info()
print("Скорость:"), bird.calcelate_speed())
print("Энергия:"), bird.calcelate_energy())


print("Рыба:")
fish.display_info()
print("Скорость:"), fish.calcelate_speed())
print("Энергия:"), fish.calcelate_energy())