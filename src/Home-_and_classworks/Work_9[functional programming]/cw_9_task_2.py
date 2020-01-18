# Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}” в другой список

print((lambda x: [f'Hello, {name}' for name in x])(['Alex', 'Masha', 'Ivan']))
