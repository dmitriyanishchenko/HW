# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое. Написать программу
# в виде трех функций.


def average(*args):
    summ = 0
    for i in range(len(args)):
        summ += args[i]
    result = summ / len(args)
    return print(f'Average in tuple {args} is {result}')


def geometric_mean(*args):
    geom = 1
    for i in range(len(args)):
        geom *= args[i]
    result = geom / len(args)
    return print(f'Geometric mean in tuple {args} is {result}')


def full_func(*args, **kwargs):
    for item in kwargs.values():
        if item == 'arifm':
            average(*args)
        elif item == 'geom':
            geometric_mean(*args)


full_func(1, 2, 3, 4, 5, mean_type='arifm')
full_func(1, 2, 3, 4, 5, mean_type='geom')
