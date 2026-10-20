#Шахов Андрей вариант 6

class Employee:
	def __init__ (self, _name, _salary):
		self._name = _name
		self._salary = _salary

	def set_name(self, _name):
		self._name = _name
		return self._name

	def set_salary(self, _salary):	
		self._salary = _salary	
		return self._salary

	def get_name(self):
		return self._name

	def get_salary(self):
		return self._salary

calss Teacher(Employee):
	def teach():
		print("Учитель преподает")
	
	def work():
		print("Учитель работает")

calss Programmer(Employee):
	def code():
		print("Програмист пишет код")

	def work():
		print("Програмист работает")

calss Doctor(Employee):
	def treat():
		print("Врач лечит пациентов")

	def work():
		print("Врач работает")

teacher = Teacher(Radion, 5)
programmer = Programer(Kiril, 4)
doctor = Doctor(Madi, 8)

Teacher.work()
Doctor.work()
Programmer.work()