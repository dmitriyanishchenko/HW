# Дан список чисел. Посчитать сколько раз встречается каждое число


def counter_num(*args):
    count = {}
    for elem in args:
        if elem in count:
            count[elem] += 1
        else:
            count[elem] = 1
    for key, value in count.items():
        return print(f'Number {key} occurs {value} times')

number = counter_num(1, 8, 7, 1, 6, 5, 2, 8)
