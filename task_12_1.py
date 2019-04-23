from utils import (
    Pet,
    Dog,
    Cat,
    Parrot
)


def voice(*args):
    for animal in args:
        if animal == 'dog':

            dog.voice()
        elif animal == 'cat':
            cat.voice()


def main():
    dog = Dog('Bob', 10, 'Dima', 7, 0.5)
    # dog.jump()
    # dog.run()
    dog.voice()
    # print(f'Name is {dog.name}')
    # print(f'Age = {dog.age}')
    # dog.birthday()
    # print(f'Age = {dog.age}')
    # print(f'Weight = {dog.weight}')
    # print(f'Height = {dog.height}')
    # print(f'{dog.master} is master {dog.name}`s')
    #####################################################################
    cat = Cat('Barsik', 5, 'Max', 2, 0.5)
    # cat.change_weight()
    # cat.change_height()
    # print(cat.weight)
    # print(cat.height)
    # cat.run()
    # cat.jump()
    cat.voice()
    # print(f'Name is {cat.name}')
    # print(f'Age = {cat.age}')
    # cat.birthday()
    # print(f'Age = {cat.age}')
    # print(f'{cat.master} is master {cat.name}`s')
    ####################################################################
    # parrot = Parrot('Kesha', 3, 'Vova', 0.03, 0.1, "cockatoo")
    # parrot.run()
    # parrot.jump()
    # parrot.fly()
    # print(parrot.weight)
    # parrot.change_weight()
    # print(parrot.weight)
    # parrot.fly()
    # print(f'Name is {parrot.name}')
    # print(f'Age = {parrot.age}')
    # parrot.birthday()
    # print(f'Age = {parrot.age}')
    # print(f'{parrot.master} is master {parrot.name}`s')
    # print(f'Species is {parrot.species}')

    print(voice('dog', 'cat'))


if __name__ == '__main__':
    main()
