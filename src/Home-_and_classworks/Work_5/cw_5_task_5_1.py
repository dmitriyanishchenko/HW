# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.

from random import randint

n = int(input("Enter the dimension of the square matrix --->"))

matrix = []
for i in range(0, n):
    row = []
    for j in range(0, n):
        row.append(randint(1, 9))
    print(row)
    matrix.append(row)
