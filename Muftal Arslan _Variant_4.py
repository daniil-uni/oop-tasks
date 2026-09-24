Муфтал Арслан ИС-24-4 
 					Вариант 4

1 задание 

class Fruit:
	def __init__ (self, name, taste):
         self.name = name
	 self.tste = taste
 	
	def discribe(self):
	 print(f"Фрукт: (self.name), вкус: {self.taste}")

fruit = fruit("яблоко", "сладкий")
fruit.discribe()


2 задание 

class Fruit:
	def __init__ (self, name, taste):
         self.name = name
	 self.tste = taste

class Apple(Fruit):
	def crunch(self):
	 print (" яблоко хрустит")

class Orange(Fruit):
	def peel(self):
	 print(" Апельсин очищается ")
Class Banana(Fruit):
	def peel(self):
	 print(" Банан очищается ")

aplle = Apple("Яблоко", "Кислый")
orange = Orange("Апельсин", "Кислый")
banana = Banana("Апельсин", "Сладкий")

apple.crunch()
orange.peel()
banana.peel()


3 задание 

сlass Fruit:
	def discribe(self):
	 print("это фрукт")

class apple 
	def discribe(self):
	 print("это яблоко")

class Orange(Fruit):
	def discribe(self):
	 print(" Это апельсин  ")

Class Banana(Fruit):
	def discribe(self):
	 print(" Это банан  ")

fruit = Fruit
aplle = Apple
orange = Orange
banana = Banana

fruit.discribe()
apple.discribe()
orange.discribe()
banana.discribe()
