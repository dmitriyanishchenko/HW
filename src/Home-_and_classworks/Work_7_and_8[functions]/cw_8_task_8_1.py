# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое. Написать программу
# в виде трех функций.



def arif(*args):
    summ = sum(args)
    arif = summ / len(args)
    return arif


def geom(*args):
    mult = 1
    for elem in args:
        mult *= elem
    geom = mult / len(args)
    return geom


def full_func(*args, **kwargs):
    for key, value in kwargs.items():
        if value == 'arif':
            result = arif(*args)
        elif value == 'geom':
            result = geom(*args)
    return result


result_func_a = full_func(1, 2, 3, 4, mean_type='arif')
result_func_g = full_func(1, 2, 3, 4, mean_type='geom')
print(result_func_a)
print(result_func_g)
