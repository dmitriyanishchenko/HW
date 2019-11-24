# Дан список чисел. Посчитать сколько раз встречается каждое число.
# Подсказка: для хранения данных использовать словарь. Для проверки нахождения элемента в
# словаре использовать метод get()
from random import randint


def count_number(*args):
    args = args[0]
    res_dict = {}
    for elem in args:
        count = 0
        for j in range(len(args)):
            if elem == args[j]:
                count += 1
        res_dict[elem] = count
    return res_dict


list_number = [randint(0, 10) for i in range(10)]
print(list_number)
print(count_number(list_number))
