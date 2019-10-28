#Дана целочисленная квадратная матрица. найти в каждой строке
# наибольший элемент и поменять его местами с элементом главной диагонали
from random import randint
i = 0
j = 0
matrix = []
n = 4
for i in range(0, n):
    row = []
    for j in range(0, n):
         row.append(randint(1, 9))
    matrix.append(row)
print(matrix)

for i in range(0, n):
    print(matrix[i])

i = 0
j = 0

for i in range(0, n):
    max_el = 0
    for j in range(0, n):
        if matrix[i][j] > max_el:
            max_el = matrix[i][j]
    matrix[i][i] = max_el
    print(max_el)

for i in range(0, n):
    print(matrix[i])
