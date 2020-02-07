# Дан список чисел. Посчитать сколько раз встречается каждое число.



def counter_num(*args):
    count = {}
    for elem in args:
        if elem in count:
            count[elem] += 1
        else:
            count[elem] = 1
    for key, value in count.items():
        return print(f'Number {key} occurs {value} times')

<<<<<<< HEAD:src/task_8_2.py
number = counter_num(1, 8, 7, 1, 6, 5, 2, 8)
=======

number = counter(1, 8, 7, 1, 6, 5, 2, 8)
>>>>>>> 0b112ffcc53a7ce08efc2038d03dad788fdeb842:src/Home-_and_classworks/Work_7_and_8[functions]/cw_8_task_8_2.py
