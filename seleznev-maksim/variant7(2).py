class Employee:
    def __init__(self, name, experience):
        self._name = name
        self.__experience = experience

    def get_experience(self):
        return self.__experience

    def display_info(self):
        print("Имя:", self._name)
        print("Опыт:", self.__experience, "лет")

    def calculate_bonus(self):
        return self.__experience * 100

    def calculate_workload(self, hours):
        return hours

class Teacher(Employee):
    def calculate_bonus(self):
        return self.get_experience() *100 * 0.10

    def calculate_workload(self, hours):
        return hours * 4

class Researcher(Employee):
    def display_info(self):
        print("Исследователь", self._name)
        print("Опыт", self.get_experience(), "лет")

    def calculate_bonus(self):
        return self.get_experience() * 100 * 0.15

    def calculate_wordload(self, hours):
        return hours / 2

class Professor(Teacher, Researcher):
    pass

professor = Professor("Иван", 10)

professor.display_info()
print("Премия:", professor.calculate_bonus())
print("Нагрузка:", professor.calculate_wordload(8))
print("Порядок поиска методов:", Professor.mro())
