# Написать программу для работы с матрицами: создание, вывод, сумма всех элементов,
# нахождение максимального, минимального элемента.
from random import randrange


def create_matrix(i, j, m, n):
    """
    this function creates a matrix of integers with dimension i by j and an interval from m to n
    :param i: number of matrix rows
    :param j: number of matrix columns
    :param m: start interval
    :param n: stop interval
    :return: matrix
    """
    matrix = []
    for row in range(i):
        row = []
        for elem in range(j):
            elem = randrange(m, n + 1)
            row.append(int(elem))
        matrix.append(row)
    return matrix


def show_matrix(matrix):
    """
    this function takes the input matrix and displays it line by line on the screen
    :param matrix:
    :return: matrix row
    """
    for row in matrix:
        print(row)


def summ_matrix(matrix):
    """
    this function takes a matrix as input and outputs the sum of all its elements
    :param matrix:
    :return: sum all elements
    """
    summ = 0
    for row in matrix:
        for elem in row:
            summ += elem
    return print(f'The sum of all elements of the matrix is {summ}')


def max_elem_matrix(matrix):
    """
    this function takes a matrix as input and returns its maximum element
    :param matrix:
    :return: maximum element
    """
    max_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_elem:
                max_elem = elem
    return print(f'The maximum element of the matrix is {max_elem}')


def min_elem_matrix(matrix):
    """
    this function takes a matrix as input and returns its maximum element
    :param matrix:
    :return: minimum element
    """
    min_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_elem:
                min_elem = elem
    return print(f'The minimum element of the matrix is {min_elem}')


i = int(input('Enter the number of rows in matrix    --->\t'))
j = int(input('Enter the number of columns in matrix --->\t'))
m = int(input('Enter the interval values:       from --->\t'))
n = int(input('Enter the interval values:       to   --->\t'))

matrix_1 = create_matrix(i, j, m, n)
show_matrix(matrix_1)
summ_matrix(matrix_1)
max_elem_matrix(matrix_1)
min_elem_matrix(matrix_1)
