# Написать функцию, которая получает на вход имя и выводит строку вида:
# “Hello, {name}”. Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.


def hello(name):
    print(f'"Hello, {name}"')


list_names = ['Petr', 'Ivan', 'Anna', 'Dmitriy', 'Svetlana']

for name in list_names:
    hello(name)
