# Создать функцию, принимающая на вход неопределенное количество аргументом и возвращающая сумму args[i] * i
# Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10


def summ_arg(*args):
    """
    This function takes an input list with an undefined number of elements
    :param args:
    :return: the sum of all arguments according to the formula args[i] * i
    """
    args = args[0]
    length = len(args)
    summ = 0
    for i in range(length):
        summ += args[i] * i
    return summ


list_a = [4, 3, 2, 1]
result = summ_arg(list_a)
print(f'Сумма равна {result}')
