# Создать функцию, которая принимает на вход неопределенное количество аргументов и возвращает
# их сумму и максимальное из них.

def summ_and_max(*args):
    args = list(args)
    length = len(args)
    print
    summ_all_elem = 0
    max_elem = args[0]
    for i in range(length):
        summ_all_elem += args[i]
        if args[i] > max_elem:
            max_elem = args[i]
    return summ_all_elem, max_elem


summ, max = summ_and_max(1, 2, 3, 4, 5)
print(f'summ is {summ}, maximum is {max}')
