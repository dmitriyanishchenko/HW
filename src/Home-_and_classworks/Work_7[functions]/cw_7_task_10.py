# Рассчитать значение х определив и использовав необходимую функции.
# х = ((sqrt(5)+5)/2)  +  ((sqrt(12)+12)/2) + ((sqrt(19)+19)/2)


def func_sqrt_elem(*args):
    args = list(args)
    print(args)
    res_list = []
    for elem in args:
        res = round((elem ** 0.5 + elem) / 2, 5)
        res_list.append(res)
    return res_list


def summ_el(*args):
    args = args[0]
    summ = 0
    for elem in args:
        summ += elem
    return summ


result_list = func_sqrt_elem(5, 12, 19)
print(result_list)
print(summ_el(result_list))
