# Дан список чисел. Вернуть список, где каждый число переведено в строку
# [5, 3] -> [‘5’, ‘3’]

numbers = [5, 3]
result = list(map(lambda x: str(x), numbers))
print(numbers, '->', result)
