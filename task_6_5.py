# В массиве целых чисел с количеством элементов 19
# определить максимальное число и заменить им все четные по значению элементы
from random import randint

row = []
for elem in range(0, 19):
    row.append(randint(-100, 100))
print(row)

max_el = 0
for elem in row:
   if elem > max_el:
       max_el = elem
print(max_el)

new_row = []
for elem in row:
    if elem%2 == 0:
        new_row.append(max_el)
    else:
        new_row.append(elem)
print(new_row)
