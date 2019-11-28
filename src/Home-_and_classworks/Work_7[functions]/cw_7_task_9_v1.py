# Дан список чисел. Посчитать сколько раз встречается каждое число.

from random import randint


def count_number(*args):
    args = sorted(args[0])
    res_dict = {}
    for elem in args:
        count = 0
        for j in range(len(args)):
            if elem == args[j]:
                count += 1
        res_dict[elem] = count
    for _, val in res_dict.items():
        print(_, ' :: ', val)


list_number = [randint(0, 9) for i in range(50)]
print(list_number)
count_number(list_number)


