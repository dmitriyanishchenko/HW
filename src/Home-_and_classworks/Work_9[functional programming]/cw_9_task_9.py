# Генератор квадратной матрицы размерностью n
from random import randint

n = 3
matrix = [[randint(0, 9) for j in range(n)] for i in range(n)]
print(matrix)
