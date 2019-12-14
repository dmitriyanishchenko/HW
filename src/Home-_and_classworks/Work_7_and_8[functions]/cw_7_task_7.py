# Создать функцию, которая принимает на вход неопределенное количество
# именных аргументов и выводит на экран те из них, длина ключа которых четна.

def func_print(**kwargs):
    for key, value in kwargs.items():
        if not len(key) % 2:
            print(key, value)

func_print(aaa=1, bb=2, cccc=3, ddddd=4)