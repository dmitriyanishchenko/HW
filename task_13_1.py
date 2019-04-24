# Создать статичный метод get_random_name в классе Pet.
#  Метод возвращает случайную строку вида А-42


from utils_for_task_13_1 import (
    Pet,
    Dog,
    Cat,
    Parrot,
    Hourse,
    Donkey,
    Mule
)


def main():
    dog = Dog('Bob', 10, 'Dima', 7, 0.5)
    # dog.jump()
    # dog.run()
    # dog.voice()
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
    # cat.voice()
    # print(f'Name is {cat.name}')
    # print(f'Age = {cat.age}')
    # cat.birthday()
    # print(f'Age = {cat.age}')
    # print(f'{cat.master} is master {cat.name}`s')
    ####################################################################
    parrot = Parrot('Kesha', 3, 'Vova', 0.03, 0.1, "cockatoo")
    mule = Mule('bbb', 3, 'sss', 6, 9)

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
    # print(Pet.get_counter())
    # mule.voice()
    # print(list(filter(lambda x: '__' not in x, dir(Pet))))
    Pet.get_random_name()
    cat.get_random_name()
    dog.get_random_name()
    parrot.get_random_name()
    mule.get_random_name()


if __name__ == '__main__':
    main()
