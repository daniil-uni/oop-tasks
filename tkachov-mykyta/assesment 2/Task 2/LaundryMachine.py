from Dryer import Dryer
from Washer import Washer

class LaundryMachine(Washer, Dryer):
	def __init__(self, capacity, model):
		super().__init__(capacity, model)

	def calculate_load(self):
		return Dryer.calculate_load(self)