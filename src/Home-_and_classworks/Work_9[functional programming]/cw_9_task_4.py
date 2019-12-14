# Дан список имен, отфильтровать все имена, где есть буква k

result = list(filter(lambda name: 'k' in name, ['Dima', 'Vova', 'Vika', 'Maks']))
print(result)
