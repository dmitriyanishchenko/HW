# Создать lambda функцию, которая принимает на вход неопределенное количество именных
# аргументов и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

my_dict = {'a': 24, 'b': 33}
print((lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(**my_dict))
