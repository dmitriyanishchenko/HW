# Создать функцию, принимающая на вход неопределенное количество аргументом и возвращающая сумму args[i] * i
# Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10


def summ_arg(*args):
    args = args[0]
    length = len(args)
    summ = 0
    for i in range(length):
        summ += args[i] * i
    return summ


list_a = [5, 4, 3, 2, 1]
print(f'Сумма всех элементов списка {list_a} равна {summ_arg(list_a)}')
