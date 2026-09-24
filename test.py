# Контрольная работа № 2, Өндіріс Бақдәулет
class ZooAnimal:
	def __init__(self, species, weight):
		self.set_data(self, species, weight)
		self.get_data()
	def set_data(self, species, weight):
		self._specise = species
		self._weight = weight
	def get_data(self):
		print("Type: ", self._specise, "Weight: ", self._weight)
	def sound(self)
		print("Издает звук")
		

class Lion(ZooAnimal):
	def __init__(self, do, Sound = None):
		self.do = do
		self.roar()

	def roar(self):
		print(self.do)

	def sound(self, Sound)	
		print()
class Elephant(ZooAnimal):
	def __init__(self, sound):
		self.sound = sound
		self.trumpet()
	def trumpet(self):
		print(self.sound)

class Penguin(ZooAnimal):
	def __init__(self, do):
		self.do = do
		self.swim()
	def swim(self):
		print(self.do)

lion1 = Lion("Лев рычит")
el = Elephant("Слон трубит")
pen = Penquin("Пингвин плавает")


	

