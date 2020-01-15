# Дан список чисел. Найти произведение всех чисел, которые кратны 3.

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = list(filter(lambda x: x % 3 == 0, numbers))

if not new_numbers:
    print(f'List {numbers} does not contain multiples of 3')
else:
    result = reduce(lambda a, x: a * x, new_numbers, 1)
    print(f'In list {numbers} the product of all numbers that are multiples of 3 is {result}')
