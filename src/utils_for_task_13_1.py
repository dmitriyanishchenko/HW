# Создать статичный метод get_random_name в классе Pet.
#  Метод возвращает случайную строку вида А-42


from random import randint


class Pet:
    __counter = 0

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True
        Pet.__counter += 1

    @classmethod
    def get_counter(cls):
        return cls.__counter

    @staticmethod
    def get_random_name():
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        return print(alphabet[randint(0, 26)] + '-' + str(randint(10, 99)))

    def run(self):
        print('Run!')

    def jump(self):
        print('Jump!')

    def birthday(self):
        self.age += 1

    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.2

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.2

    def voice(self):
        pass


class Dog(Pet):

    def voice(self):
        print('Woof! Woof!')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 13:
                self.is_alive = False


def call_voice(animals):
    for animal in animals:
        animal.voice()


class Cat(Pet):

    def voice(self):
        print('Meow! Meow!')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 16:
                self.is_alive = False


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def fly(self):
        if self.weight > 0.1:
            print('this parrot cannot fly')
        else:
            print('fly')

    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.05

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.05

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 60:
                self.is_alive = False


class Hourse(Pet):
    def voice(self):
        print('Igo-goo')


class Donkey(Pet):
    def voice(self):
        print('Ia-ia')


class Mule(Donkey, Hourse):
    pass
