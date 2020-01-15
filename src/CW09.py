# генератор списков
# list_a = [i  for i in range(5)]#
# print(list_a)
# *****************************************************************

# task 9 1 Дан список слов. Сгенерировать новый список с перевернутыми словами

# list_a = ['word', 'papa', 'mama']
#
# list_b = [word[::-1] for word in list_a]
# print(list_b)
# >>>>
# *********************************************************************
# task_9_2 Дан список словарей. Каждый словарь описывает машину(серийный номер и год выпуска).
#  Создать новый список со всеми машинами, год выпуска которых больше n
#
# list_car = [
#
#     dict(number='01', year=1996),
#     dict(number='02', year=1997),
#     dict(number='03', year=1998),
#     dict(number='04', year=1999),
#     dict(number='05', year=2000)
#
# ]
#
# list_car_2 = [car for car in list_car if car['year'] > 1998]
# print(list_car_2)
# *****************************************************************************
# Генератор квадратной матрицы
# from random import randint
# n = 3
# matrix = [[randint(0, 9) for j in range(n)] for i in range(n)]
# print(matrix)
#
# ****************************************************************************
# генератор словарей
# old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
# new_dict = {key + str(len(key)): value for key, value in old_dict.items()}
# print(new_dict)
#
# ***************************************************************
# Дан словарь, создать новый словарь, поменяв местам ключ и значение
#
# old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
# new_dict = {value: key for key, value in old_dict.items()}
# print(new_dict)
# ****************************************************
# lambda выражения
# print((lambda x, y, z: x + y + z)(1, 2, 3))
# ****************************************************************************************
# Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”
#
#
# print((lambda name: f'hello, {name}')('max'))
#
# ************************************************************************************
# Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}”


# print((lambda names: [f' hello, {name}' for name in names])(['vova', 'kolya', 'masha']))

from datetime import datetime
from time import sleep


def time_decorator(func):
    def do_some_staff(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f'Func time  is: {end - start}')
        return result

    return do_some_staff


@time_decorator
def sleep_func(n):
    sleep(n)
    return 'a'


print(sleep_func(5))
