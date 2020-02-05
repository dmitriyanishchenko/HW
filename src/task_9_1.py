#  Дан список строк. Отформатировать все строки в формате '{i} - {string}, где  это порядковый
#  номер строки в списке. Использовать генератор списков.

from random import randint

n = 5
matrix = [[randint(1, 9) for j in range(n)] for i in range(n)]
print(matrix)

count = 0
for row in matrix:
    print(f'{count} - {row}')
    count += 1
