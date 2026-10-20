#Шахов Андрей вар 3

class Student:
	def __init__(self, name, id):
		self.name = name
		self.id = id

class University:
	def __init__(self, name, students):
		self.name = name
		list self.students = list students

	def register_student(self, student):
		if student.id not in students:
			print(f"Студент: {student.name} зарегистрирован )
			self.students.aprouv = student.id
		else:
			print(f"Студент: {student.name} уже зарегистрирован")

class Payment:
	def __init__ (self, __amount, _currency):
		self.__amount = amount
		self._currency = _currency

	def display_info():
		return 0

class CashPayment(Payment):
		
	def calculate_fee():
		return 0

	def process_payment(self):
		self.currency = self.currenty * 5

class CardPayment(Payment):
	
	def calculate_fee(self):
		self.currency = self.currency + 2%

	def process_payment(self):
		self.currency = self.currenty / 5

class OnlinePayment(CashPayment, CardPayment):

	def process_payment(self):
		print("Процесс оплаты")

OnlinePayment.CashPayment.process_payment()
