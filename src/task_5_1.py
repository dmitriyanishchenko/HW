# Дана целочисленная матрица размером 5х5. Получить новую матрицу
# путем деления всех элементов данной матрицы на ее наибольший по
# модулю элемент

from random import randint


print("Введите интервал значений для матрицы")
a = int(input("от:\n  \t"))
b = int(input("до: "))

i = 0
j = 0
old_matrix = []
for i in range(0, 5):
    row = []
    for j in range(0, 5):
        row.append(randint(a, b))
    old_matrix.append(row)

for row_1 in old_matrix:
    print(row_1)

max_value = 0
for i in range(0, 5):
    for j in range(0, 5):
        k = abs(old_matrix[i][j])
        if k > max_value:
            max_value = old_matrix[i][j]

matrix = []
el = 0
for i in range(0, 5):
    row = []
    for j in range(0, 5):
        el = round(old_matrix[i][j] / max_value, 2)
        row.append(str(el))
    matrix.append(row)

for i in range(0, 5):
    print(' '.join(matrix[i]))
