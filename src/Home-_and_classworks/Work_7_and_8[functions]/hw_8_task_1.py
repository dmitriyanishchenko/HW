# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n,
# если n — четное (n > 0 — параметр целого типа. С помощью этой функции найти двойные факториалы
# пяти данных целых чисел

def fact2(n):
    res = 1
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            res *= i
        return print(f'{n}n!! = {res}')

    else:
        for i in range(1, n + 1, 2):
            res *= i
        return print(f'{n}n!! = {res}')


list_number = [1, 2, 3, 4, 5, 6]
for num in list_number:
    fact2(num)
