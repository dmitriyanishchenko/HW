# Дан список чисел. Посчитать сколько раз встречается каждое число.


def counter(*args):
    print(args)
    count = {}
    for elem in args:
        if elem in count:
            count[elem] += 1
        else:
            count[elem] = 1
    return count


number = counter(1, 8, 7, 1, 6, 5, 2, 8)

for key, value in number.items():
    print(f'Number {key} occurs {value} times')