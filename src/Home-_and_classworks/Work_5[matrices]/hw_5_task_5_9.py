# Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.

from random import randint

matrix = []

for i in range(5):
    row = []
    for j in range(5):
        elem = randint(0, 9)
        row.append(elem)
    matrix.append(row)
    print(row)

for i in range(5):
    max_elem = 0
    for j in range(5):
        if matrix[i][j] > max_elem:
            max_elem = matrix[i][j]

    matrix[i][i] = max_elem
    print(f'In line #{i} the maximum element is {max_elem}')

for row in matrix:
    print(row)
