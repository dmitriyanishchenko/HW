# 1. Создать два списка a = [1,2,3,4] и b = [ ]
# 2. Вывести на экран id a и b
# 3. Присвоить b значение a (b=a)
# 4. Вывести на экран id переменных
# 5. Добавить элемент в список b
# 6. Вывести на экран оба списка

a = [1, 2, 3, 4]
b = []
print(f'list a->{a}            list b->{b}')
print(f'id(a) ->{id(a)}         id(b) ->{id(b)}')
b = a
print(f'id(a) ->{id(a)}         id(b) ->{id(b)}')
b.append(5)
print(f'list a->{a}         list b->{b}')