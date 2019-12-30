# Дан двумерный массив n × m элементов. Определить, сколько раз встречается число 7 среди элементов массива

from random import randrange

print('Set the size of a two-dimensional array from n do m')
n = int(input('n ---> \t'))
m = int(input('m ---> \t'))

matrix = []
for i in range(0, n):
    row = []
    for j in range(0, m):
        row.append(randrange(0, 10))
    print(row)
    matrix.append(row)

counter = 0
for row in matrix:
    for elem in row:
        if elem == 7:
            counter += 1
print(f'numbers 7 in this array is {counter}')
