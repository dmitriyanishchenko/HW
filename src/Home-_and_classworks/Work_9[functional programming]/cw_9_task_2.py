# Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}” в другой список

names = ['Vova', 'Masha', 'Ivan', 'Tanja', ]

# Var. 1
result = []
for name in names:
    res_string = lambda x, y: x + y
    elem = res_string('Hello, ', name)
    result.append(elem)
print(result)

# Var. 2
print((lambda names: [f'Hello, {name}' for name in names])(names))

