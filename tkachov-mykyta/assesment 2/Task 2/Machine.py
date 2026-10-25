class Machine:
	def __init__(self, capacity, model):
		self.__capacity = capacity
		self._model = model

	def display_info(self):
		print("Model: ", self._model, ", capacity: ", self.__capacity)

	def calculate_load(self):
		pass

	def calculate_energy(self):
		pass