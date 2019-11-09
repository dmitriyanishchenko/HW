# Дана целочисленная матрица размера 5х5. Получить новую матрицу
# путем деления всех элементов данной матрицы на ее наибольший по
# модулю элемент.

from random import randrange

matrix_start = []
for row in range(5):
    row = []
    for elem in range(5):
        elem = randrange(-10, 10)
        row.append(elem)
    matrix_start.append(row)
    print(row)

max_elem = 0
for row in matrix_start:
    for elem in row:
        if abs(elem) > abs(max_elem):
            max_elem = abs(elem)
print(max_elem)

matrix_res = []
for row in matrix_start:
    matrix_res_row = []
    for elem in row:
        elem_res = round(elem / max_elem, 2)
        matrix_res_row.append(elem_res)
    matrix_res.append(matrix_res_row)
    print(matrix_res_row)
