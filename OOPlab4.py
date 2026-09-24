class Fruit:
    def __init__(self, name: str, taste: str):
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
    def __init__(self, name="Яблоко", taste="сладкий"):
        super().__init__(name, taste)

    def crunch(self):
        print("Яблоко хрустит")

    def describe(self):
        print("Яблоко хрустит и это фрукт")


class Orange(Fruit):
    def __init__(self, name="Апельсин", taste="кисло-сладкий"):
        super().__init__(name, taste)

    def peel(self):
        print("Апельсин очищается")

    def describe(self):
        print("Сочный апельсин")


class Banana(Fruit):
    def __init__(self, name="Банан", taste="сладкий"):
        super().__init__(name, taste)

    def peel(self):
        print("Банан очищается")

    def describe(self):
        print("Спелый банан")


if __name__ == "__main__":
    parent_fruit: Fruit = Fruit("Фрукт", "обычный")
    child_apple: Fruit = Apple()
    child_orange: Fruit = Orange()
    child_banana: Fruit = Banana()

    parent_fruit.describe()
    child_apple.describe()
    child_orange.describe()
    child_banana.describe()