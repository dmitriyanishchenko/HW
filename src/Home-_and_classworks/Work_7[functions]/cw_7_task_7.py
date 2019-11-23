# Создать функцию, которая принимает на вход неопределенное количество именных аргументов и выводит на экран
# те из них, длина ключа которых четна.

def arg_leven_key_length(**kwargs):
    for key, value in kwargs.items():
        if not len(key) % 2:
            print(key, value)


arg_leven_key_length(aaa=1, bbbbbb=2, cccc=3, ddddd=4)
