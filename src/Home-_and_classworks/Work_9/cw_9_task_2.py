# Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}” в другой список

names = ['Vova', 'Masha', 'Ivan', 'Tanja']
result = []
for name in names:
    res_string = lambda x, y: x + y
    elem = res_string('Hello, ', name)
    result.append(elem)
print(result)
