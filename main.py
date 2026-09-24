#номер4 
Class Fruit:
    def __init__(self, name, taste):
        self._name = name
        self._taste = taste

    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, value):
        self._name = value

    
    @property
    def taste(self):
        return self._taste

        
    @taste.setter
    def taste(self, value):
        self._taste = value

    
    def describe(self):
        print("Это фрукт")



class Apple(Fruit):
    def crunch(self):
        print("Яблоко хрустит")

    def describe(self):
        print("Это яблоко")



class Orange(Fruit):
    def peel(self):
        print("Апельсин очищается")

    def describe(self):
        print("Это апельсин")



class Banana(Fruit):
    def peel(self):
        print("Банан очищается")

    def describe(self):
        print("Это банан")


apple = Apple("Яблоко", "сладкое")
orange = Orange("Апельсин", "кисло-сладкий")
banana = Banana("Банан", "сладкий")



print("Название:", apple.name)
print("Вкус:", apple.taste)

apple.name = "Красное яблоко"
apple.taste = "очень сладкое"

print("Новое название:", apple.name)
print("Новый вкус:", apple.taste)



apple.crunch()
orange.peel()
banana.peel()


print("\nМетод describe:")

fruit1 = apple
fruit2 = orange
fruit3 = banana

fruit1.describe()
fruit2.describe()
fruit3.describe()