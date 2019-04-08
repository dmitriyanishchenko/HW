# Описать функцию вещественного типа , вычисляющую двойной факториал n!! = 1 * 3 * 5 * ... * n , если  n-нечетное;
# n!! = 2 * 4 * 6 * ... * n, если n четное ( n > 0 - параметр целого типа). С помощью этой функции найти двойные
# факториалы пяти данных чисел


def fact2(*args):
    for arg in args:
        fact = 1
        if not arg % 2:
            for elem in range(2, arg + 1, 2):
                fact *= elem
            print(f'n!! number {arg} = {fact}')
        else:
            for elem in range(1, arg + 1, 2):
                fact *= elem
            print(f'n!! number {arg} = {fact}')


n = fact2(2, 7, 10, 13, 22)
