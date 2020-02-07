# Написать декоратор, который будет выводить время выполнения функции. Задать две любые функции и отобразить
# время их выполнения

from datetime import datetime
from time import sleep

import functools


def time_decorator(func):
    @functools.wraps(func)
    def do_some_staff(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f'Func time is: {end - start}')
        return result

    return do_some_staff


@time_decorator
def sleep_func(n):
    sleep(n)
    return 'a'


@time_decorator
def count(a, b):
    return a + b


print(sleep_func(1))
print(sleep_func.__name__)
print('_' * 50)
print(count(5, 6))
print(count.__name__)
