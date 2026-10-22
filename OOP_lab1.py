class Employee:
	def __init__(self, name, salary):
		self.__name = name
		self.__salary = salary

	def get_name(self):
		return self.__name

	def get_salary(self):
		return self.__salary

	def set_name(self, name):
		self.__name = name

	def set_salary(self, salary):
		self.__salary = salary

class Teacher(Employee):
	def teach(self):
		print("Учитель преподает")
		return

	def work(self):
		print("Учитель работает")
		return

class Programmer(Employee):
	def code(self):
		print("Программист пишет код")
		return
	
	def work(self):
		print("Программист работает")
		return

class Doctor(Employee):
	def treat(self):
		print("Врач лечит пациента")
		return

	def work(self):
		print("Врач работает")
		return

teacher = Teacher("Иванов", 200000)
programmer = Programmer("Петров", 300000)
doctor = Doctor("Сидоров", 250000)

teacher.teach()
programmer.code()
doctor.treat()

objects = [teacher, programmer, doctor]

for object in objects:
    object.work()
	