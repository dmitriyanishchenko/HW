# Рассчитать значение х определив и использовав необходимую функцию
#  х = ((sqrt(5)+5)/2)  +  ((sqrt(12)+12)/2) + ((sqrt(19)+19)/2)

def my_func(*args):
    summ = 0
    for elem in args:
        res = round((elem ** 0.5 + elem) / 2, 3)
        summ += res
    return summ


a = my_func(5, 12, 19)
print(a)
