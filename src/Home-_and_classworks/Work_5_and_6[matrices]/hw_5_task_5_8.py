# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего).

from random import randint

row = []
for i in range(10):
    row.append(randint(0, 9))

result = 0
count = 0
for j in range(0, len(row) - 2):
    if row[j + 1] > row[j]:  # начало участка
        count += 1
        if count >= 1 and row[j + 2] < row[j + 1]:  # konez uchastka
            result += 1
            count = 0

if row[-2] < row[-1]:
    result += 1
print(f'In list {row}  {result} monotonously increasing sections')
