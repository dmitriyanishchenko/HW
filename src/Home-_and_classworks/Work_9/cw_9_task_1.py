# Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”

name = input('Enter your name --->\t')
func = lambda x, y: x + y
print(func('Hello, ', name))
