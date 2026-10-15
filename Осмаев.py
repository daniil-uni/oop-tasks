class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Книга добавлена в библиотеку")

    def lend_book(self, title):
        for b in self.books:
            if b.title == title:
                self.books.remove(b)
                print(f"Книга '{b.title}' выдана читателю")
                return b
        print("Такой книги нет")


b1 = Book("Мастер и Маргарита", "Булгаков")
lib = Library()
lib.add_book(b1)
lib.lend_book("Мастер и Маргарита")


class Device:
    def __init__(self, model, power):
        self.__model = model
        self._power = power

    def get_model(self):
        return self.__model

    def turn_on(self):
        print("Устройство включено")


class Computer(Device):
    def turn_on(self):
        print("Компьютер включен")

    def display_info(self):
        print("Модель компьютера:", self.get_model(), "Мощность:", self._power)

    def calculate_time(self):
        return self._power * 5


class Printer(Device):
    def __init__(self, model, power, speed):
        super().__init__(model, power)
        self.speed = speed

    def turn_on(self):
        print("Принтер включен")

    def display_info(self):
        print("Модель принтера:", self.get_model(), "Скорость печати:", self.speed)

    def calculate_time(self):
        return self._power / 2


class OfficeDevice(Computer, Printer):
    def __init__(self, model, power, speed):
        Device.__init__(self, model, power)
        self.speed = speed


dev = OfficeDevice("HP LaserJet", 400, 30)
dev.display_info()
print("Время работы:", dev.calculate_time())

Computer.turn_on(dev)

print(dev.get_model)
print("Порядок классов:", OfficeDevice.mro())
