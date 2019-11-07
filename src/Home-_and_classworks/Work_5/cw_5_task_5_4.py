# Дана целочисленная матрица А[n,m]. Посчитать количество элементов матрицы,
# превосходящих среднее арифметическое значение элементов матрицы и сумма индексов которых четна
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

summ_elem_matrix = 0
for row in matrix:
    for i, elem in enumerate(row):
        summ_elem_matrix += elem
print(f'The sum of the elements of the matrix is {summ_elem_matrix}')
mean_summ_elem = summ_elem_matrix / (n * m)
print(f'Arithmetic mean of matrix elements is {round(mean_summ_elem, 4)}')

counter = 0
for i, row in enumerate(matrix):
    for j, elem in enumerate(row):
        if elem > mean_summ_elem and ((i + j) % 2 == 0):
            print(f'element {elem} - index {i}:{j}')
            counter += 1
print(f'The number of matrix elements corresponding to the problem condition is {counter}')
