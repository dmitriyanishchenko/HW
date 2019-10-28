# Дан массив целых чисел А. Найти суммы положительных и отрицательных элементов
# массива, использовав функцию определения суммы

from random import randint


def summ_elem(*args):
    summ = sum(args)
    return summ


row = []
for i in range(1, 20):
    elem = int(randint(-100, 100))
    row.append(elem)
print(row)

row_pos = []
row_neg = []

for elem in row:
    if elem > 0:
        row_pos.append(elem)

    elif elem < 0:
        row_neg.append(elem)

print(row_pos)
print(row_neg)

sum_pos = summ_elem(*row_pos)
sum_neg = summ_elem(*row_neg)

print(sum_pos, sum_neg)
