# Описать функцию is_power_n(k, n) логического типа , возвращающую True,  если целый параметр
# k(>0) является степенью числа n(>1), и False в противном случае.
# Дано число n(>1)  и набор из 10 целых положительных чисел. C помощью функции is_power_n
# найти количество степеней числа n в данном наборе


import math


def is_power_n(*args):
    for arg in args:
        if int(math.log(arg, n)) == math.log(arg, n):
            print(f'{arg} is power {n}')


n = 3
result = is_power_n(2, 3, 4, 81, 16, 7, 8, 9, 10, 12)
print(result)
