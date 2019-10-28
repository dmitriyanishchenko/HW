class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True


    def run(self):
        print('run')

    def jump(self):
        print('jump')

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


class Dog(Pet):

    def bark(self):
        print('bark')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 13:
                self.is_alive = False


class Cat(Pet):


    def meow(self):
        print('meow')

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
            print('parrot not fly')
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
            self.height += 0.2

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 60:
                self.is_alive = False


def main():
    dog = Dog('Jack', 10, 'Max', 5, 7)
    cat = Cat('Bars', 5, 'Bob',  10, 5)
    parrot = Parrot('aaaa', 2, 'Vova', 0.1, 2, 'blue')
    print(parrot.weight)
    parrot.change_weight()
    print(parrot.weight)
    parrot.fly()
    # cat.meow()
    # dog.bark()
    # print(dog.name)
    # print(dog.age)
    # print(dog.master)
    # print(cat.name)
    # print(cat.age)
    # print(cat.master)
    # print(parrot.name)
    # print(parrot.age)
    # print(parrot.master)
    # print(parrot.weight)




if __name__ == '__main__':
    main()
