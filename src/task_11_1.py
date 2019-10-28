# Создать пять классов описывающие  реальные объекты.
# Каждый класс должен содержать минимум три приватнх атрибута,
# конструктор, геттеры, сеттеры для каждого атрибута, два метода


def main():
    class Elefant:
        def __init__(self, name, weight, age):
            self.__name = name
            self.__weight = weight
            self.__age = age

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, name):
            self.__name = name

        @property
        def weight(self):
            return self.__weight

        @weight.setter
        def weight(self, weight):
            self.__weight = weight

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, age):
            self.__age = age

        def walk(self):
            print('Top Top')

        def sleep(self):
            print('ZZZzzzz...')

    elefant_1 = Elefant('Toppsy', 500, 25)

    elefant_1.name = 'Taddy'

    print(elefant_1.name)
    print(elefant_1.weight)
    elefant_1.age = 20
    print(elefant_1.age)


if __name__ == '__main__':
    main()
