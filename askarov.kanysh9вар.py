#1 задание
class Member
    def __init__(self, name, age):
        self.name = name
        self.name = age


class Club:
    def __init__(self, name):
        self.name = name
        self.members = []
    
    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} добавленв клуб {self.name}")

    def show_members(self):
        print(f"\nУчастники клуба {self.name}:")
        for member in self.members:
            print(f"Имя: {member.name}, возраст: {member.age}")


member1 = Member("Арслан" 20)
member2 = Member("Нурай" 19)

club1 = Club("Программирование")
club2 = Club("Спорт")

club1.add_member(member1)
club1.add_member(member2)
club2.add_member(member1)

club1.show_members()
club2.show_members()

#2 задание
class Account
    def __init__(self, owner, balance):
        self._owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def display_info(self):
        print(f"Владелец: {self.owner}")
        print(f"Баланс: {self.__balance}")

    def calculate_interest(self):
        return 0

    def calculate_limit(self):
        return self.get_balance()


class SavingsAcccount(Account):
    def calculate_interest(self):
        return self.get_balance * 0.05

    def calculate_limit(self):
        return self.get_balance * 2

class BusinessAccount(Account):
    def calculate_interest(self):
        return self.get_balance * 0.10

    def calculate_limit(self):
        return self.get_balance / 4

дальше не успел