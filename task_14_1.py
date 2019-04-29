# Создать иерархию(слайды 49-50).
# Добавить конструктор в родительский класс Animal.
# Добавить абстрактный метод voice в класс Animal.
# Переопределить метод voice в классах Dog, Wold, Lion, Cat.
# Добавить два абстрактных метода в интерфейсы.
# Переопределить их в дочерних классах.
# Создать объекты классов Dog, Wolf, Lion, Cat.
# Вызвать каждый из метод каждого объекта.


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, suit, weight, height, age):
        self.suit = suit
        self.weight = weight
        self.height = height
        self.age = age

    @abstractmethod
    def voice(self):
        pass


class Pet(Animal):
    pass


class WildAnimal(Animal):
    pass


class FelineInterface(ABC):  # cath
    @abstractmethod
    def scratch(self):
        raise NotImplemented

    @abstractmethod
    def night_vision(self):
        raise NotImplemented


class CanineInterface(ABC):
    @abstractmethod
    def hunt(self):
        raise NotImplemented

    @abstractmethod
    def swimming(self):
        raise NotImplemented


class Cat(Pet, FelineInterface):
    def voice(self):
        print('Meow!')

    def scratch(self):
        print('Scratch!')

    def night_vision(self):
        print('Night vision!')


class Dog(Pet, CanineInterface):
    def voice(self):
        print('Woof!')

    def hunt(self):
        print('Hunt!')

    def swimming(self):
        print('Swimming!')


class Lion(WildAnimal, FelineInterface):
    def voice(self):
        print('Rrrr!')

    def scratch(self):
        print('Scratch!')

    def night_vision(self):
        print('Night vision!')


class Wolf(WildAnimal, CanineInterface):
    def voice(self):
        print('Woo!')

    def hunt(self):
        print('Hunt!')

    def swimming(self):
        print('Swimming!')


def main():
    # cat_1 = Cat('white', 0.5, 0.2, 5)
    # cat_1.night_vision()
    # cat_1.scratch()
    # cat_1.voice()

    # dog_1 = Dog('spotted', 3, 0.8, 7)
    # dog_1.voice()
    # dog_1.hunt()
    # dog_1.swimming()

    # lion_1 = Lion('redhead', 80, 1, 6)
    # lion_1.night_vision()
    # lion_1.scratch()
    # lion_1.voice()
    #

    wolf_1 = Wolf('gray', 20, 0.6, 4)
    wolf_1.voice()
    wolf_1.hunt()
    wolf_1.swimming()


if __name__ == '__main__':
    main()
