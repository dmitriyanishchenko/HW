from random import randint

n = 5


def create_matrix(n):
    matrix = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append(randint(1, 9))
        matrix.append(row)
    return matrix


a = create_matrix(5)


def simple_print(matrix):
    for row in matrix:
        print(row)


matrix_a = create_matrix(5)
simple_print(matrix_a)


def summ_matrix(matrix):
    summ = 0
    for row in matrix:
        for elem in row:
            summ += elem
    return summ


b = summ_matrix(matrix_a)
print(b)


def max_el(matrix):
    max_elem = 0
    for row in matrix:
        for elem in row:
            if elem > max_elem:
                max_elem = elem
    return max_elem


d = max_el(matrix_a)
print(d)


def minim_el(matrix):
    min_el = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_el:
                min_el = elem
    return min_el


e = minim_el(matrix_a)
print(e)

#
# def fact(n):# функция нахождение факториала числа n
#     result = 1
#     for elem in range(1, n+1):
#         result *= elem
#     return result
# print(fact(10))


# def my_func(name):
#     print(f'Hello, {name}')
#
# list_name = ['Wowa', 'Vanya', 'Denis', 'Sveta', 'Maksim']
# for name in list_name:
#     my_func(name)
