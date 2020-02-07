# lambda выражения

print((lambda x, y, z: x + y + z)(1, 2, 3))

# Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”

print((lambda name: f'Hello, {name}')('Max'))
