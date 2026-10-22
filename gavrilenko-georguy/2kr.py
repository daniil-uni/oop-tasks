#Вариант 9

#1
class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_member(self):
        print("Участник добавлен:", self.name)

    def display_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)

member1 = Member("Иван", 20)
member1.add_member()
member1.display_info()


#2
class Account:
    def __init__(self, owner, balance):
        self._owner = owner
        self.__balance = balance

    def display_info(self):
        print("Владелец:", self._owner)
        print("Баланс:", self.__balance)

class SavingsAccount(Account):
    def calculate_interest(self):
        print("Проценты: 5%")

class BusinessAccount(Account):
    def calculate_interest(self):
        print("Проценты: 10%")

class PremiumAccount(SavingsAccount, BusinessAccount):
    def calculate_interest(self):
        print("Проценты: 15%")

account = PremiumAccount("Иван", 10000)
account.display_info()
account.calculate_interest()