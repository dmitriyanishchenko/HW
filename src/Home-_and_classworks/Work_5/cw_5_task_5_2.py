# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями.
# Найти сумму всех элементов матрицы, которые кратны 3.

from random import randrange

n = int(input("Enter the dimension of the square matrix ---> \t"))

matrix = []
for i in range(0, n):
    row = []
    for j in range(0, n):
        row.append(randrange(0, 10))
    print(row)
    matrix.append(row)
summ = 0
for row in matrix:
    for elem in row:
        if elem % 3 == 0:
            summ += elem
print(f'The sum of all elements of the matrix that are multiples of 3 is {summ}')
