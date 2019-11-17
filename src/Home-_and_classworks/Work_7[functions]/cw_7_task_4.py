# Реализовать функцию возвращающую матрицу.
# На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1), random_to(по-умолчанию(9)).


from random import randint


def create_matrix(n, random_from=1, random_to=9):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(random_from, random_to))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()

def sum_matrix(matrix):
    summ = 0
    for row in matrix:
        for elem in matrix:
            summ += elem
    return summ

matrix_a = create_matrix(5, 100, 199)
print_matrix(matrix_a)

matrix_b = create_matrix(5, 5)
print_matrix(matrix_b)
