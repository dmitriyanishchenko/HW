# Описать функцию is_power_n(k, n) логического типа , возвращающую True,  если целый параметр
# k(>0) является степенью числа n(>1), и False в противном случае.
# Дано число n(>1)  и набор из 10 целых положительных чисел. C помощью функции is_power_n
# найти количество степеней числа n в данном наборе

import math


def is_power_n(k, n):
    if math.log(k, n) == int(math.log(k, n)):
        result = True
    else:
        result = False
    return result


n = 2
numbers = [3, 25, 4, 81, 16, 6, 256, 1024, 36, 77]

res_row = []
for num in numbers:
    if is_power_n(num, n):
        res_row.append(num)
count = len(res_row)

if not res_row:
    print(f'In the list {numbers} no numbers are a power of {n}')
else:
    print(f'In the list {numbers} {count} degrees of the number {n}. These are numbers {res_row}')
