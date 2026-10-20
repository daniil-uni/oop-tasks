class Employee:
	def __init__(self, name, salary):
		self.__name = name
		self.__salary = salary

	def get_name(self):
		return name

	def get_salary(self):
		return salary

	def set_name(self):
		self.__name = name

	def set_salary(self):
		self.__salary = salary

class Teacher(Employee):
	def teach():
		print("Учитель преподает")
		return

	def work():
		print("Учитель работает")
		return

class Programmer(Employee):
	def code():
		print("Программист пишет код")
		return
	
	def work():
		print("Программист работает")
		return

class Doctor(Employee):
	def treat():
		print("Врач лечит пациента")
		return

	def work():
		print("Врач работает")
		return

Teacher.teach()
Programmer.code()
Doctor.treat()

objects = ["Teacher", "Programmer", "Doctor"]

for object in objects:
	object.work

