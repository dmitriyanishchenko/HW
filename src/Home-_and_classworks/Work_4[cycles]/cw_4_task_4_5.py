# Написать программу, которая будет выводить на экран случайные числа
# от 1 до 10 до тех пор, пока не выпадет 7.

from random import randint

while True:
    rand_int = randint(1, 10)
    print(rand_int)
    if rand_int == 7:
        break
