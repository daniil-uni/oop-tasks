class Machine:
	def __init__(self, capacity, model):
		self.__capacity = capacity
		self._model = model

	def display_info(self):
		print("Model: ", model, ", capacity: ", capacity)

	def calculate_load(self):
		pass

	def calculate_energy(self):
		pass