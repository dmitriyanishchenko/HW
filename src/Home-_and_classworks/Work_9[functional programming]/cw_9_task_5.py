# Дан список чисел. Найти произведение всех чисел, которые кратны 3.

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_numbers = list(filter(lambda x: x % 3 == 0, numbers))
result = reduce(lambda a, x: a * x, new_numbers, 1)

print(new_numbers)
print(result)
