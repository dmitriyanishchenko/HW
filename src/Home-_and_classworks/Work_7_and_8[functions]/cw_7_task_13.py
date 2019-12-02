# Дан массив целых чисел A. Найти суммы положительных и отрицательных элементов массива,
# используя функцию определения суммы


from random import randint


def summ_elem(*args):
    summ = sum(args)
    return summ


row = []
for i in range(1, 10):
    elem = int(randint(-9, 9))
    row.append(elem)
print(f'Massive A: {row}')

row_pos = []
row_neg = []
for elem in row:
    if elem > 0:
        row_pos.append(elem)
    elif elem < 0:
        row_neg.append(elem)

sum_pos = summ_elem(*row_pos)
sum_neg = summ_elem(*row_neg)

print(f'Array of positive elements ---> {row_pos}. The amount is {sum_pos}')
print(f'Array of negative elements ---> {row_neg}. The amount is {sum_neg}')
