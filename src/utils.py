class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True

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
        return voice


class Dog(Pet):

    def voice(self):
        print('Woof! Woof!')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 13:
                self.is_alive = False


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
