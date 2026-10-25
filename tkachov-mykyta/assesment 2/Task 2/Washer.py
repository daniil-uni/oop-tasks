from Machine import Machine

class Washer(Machine):
	def __init__(self, capacity, model):
		super().__init__(capacity, model)

	def calculate_load(self):
		return self._Machine__capacity * 2

	def calculate_energy(self):
		return self._Machine__capacity / 2