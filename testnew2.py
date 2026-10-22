# 6 вариант 1 задание
class Patient:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Hospital:
    def add_patient (self, patient):
        self.list_p = []
        self.list_p.append(patient)

    def get_pat (self):
        print(self.list_p)

pat1 = Patient("Баха", 1)
hos = Hospital()
hos.add_patient(pat1.name)
hos.get_pat()
# 2 вариант

class Vehicle:
    def __init__(self, speed, brand):
        self.__speed = speed
        self.__brand = brand
    def display_info(self):
        print("Скорость и марка машины:", self.__speed, self.__brand)
    def get_inf(self):
        return self.__speed


class Motocycle(Vehicle):
    def calculate_distance(self):
        return self.get_inf() * 3
    def calculate_fuel(self):
        return self.get_inf() / 2


class Truck(Vehicle):
    def calculate_distance(self):
        return self.get_inf() * 2
    def calculate_fuel(self):
        return self.get_inf() * 4
    def get_inf_tru(self):
        print("Расстоя:", self.calculate_distance())
        print("Топлив:", self.calculate_fuel())


class SpecialVehicle(Motocycle, Truck):
    pass


spe = SpecialVehicle(10, "Mers")

spe.display_info()
spe.get_inf_tru()

