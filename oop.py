# Вариант 1
# Задание 1

class Truck:
	speed = 80
	def deliver(self, cargo: str) -> str:
		return f'Грузовик везет "{cargo}" по дороге'

class Ship:
	speed = 30
	def deliver(self,cargo: str) -> str:
		return f'Корабль везет"{cargo}" по морю'

class Plane:
	speed = 800
	def deliver(self,cargo: str) -> str:
		return f'Самолет везет"{cargo}" по воздуху'

class Logistics:
	def create_transport(self):
		raise NotImplementedError

	def plan_delivery(self, cargo: str, distance_km: int) -> str:
		transport = self.create_trancport()
		hours = distance_km / transport.speed
		return f'{transport.deliver(cargo)}, в пути {hours:.1f}'

class RoadLogistics(Logistics):
	truck = Truck()

	def get_logistics(kind):
		if kind = 'roat':
			return truck	
		elif:
			print(f'Ошибка: неизвестный вид логистики {kind}')

class SeeLogistics(Logistics):
	ship = Ship()
	
	def get_logistics(kind):
		if kind = 'see':
			return ship	
		elif:
			print(f'Ошибка: неизвестный вид логистики {kind}')
		
class AirLogistics(Logistics):
	plane = Plane()
	
	def get_logistics(kind):
		if kind = 'air':
			return plane		
		elif:
			print(f'Ошибка: неизвестный вид логистики {kind}')
		
if __name__ == '__main__':
	for kind in ('road', 'sea', 'air'):
		print(get_logistics(kind).plan_delivery('Мебель', 2400))
	try:
		get_logistics('train')
	except ValueError as e:
		print('Ошибка:' , e)

''' Задание 2

from PyQt.QtWindgets import QWidget, QLineEdit, QLandel, QPushButton, QVBoxLayout

class Salarywindow(QWidget):
	def __init__(self):
		super().__init__()
		self.input = QLineEdit()
		self.result = QLabel()
		btn = QPushButton('Рассчитать')
		btn.clicked.connect(self.on_click)
		layout = QVBoxLayout(self)
		for w in (self.input, btn, self.result):
			layout.addWidget(w)

	def on_click(self):
		base = float(self.input.text())
		tax = base * 0.1
		pension = base - tax - pension
		self.result.setText(f'На руки: {net}')
		with open('salary.csv', 'a', encoding='utf-8') as f:
			f.write(f'{base};{net}\n')

Нарушен принципы SOLID: класс Salarywindow выполняет сразу три задачи: управление графическим интерфейсом, расчёт заработной платы и сохранение данных в CSV-файл. '''