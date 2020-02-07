# Написать игру. Пользователь должен угадать число. Сперва вводиться диапазон угадывания.
#  После колличество попыток. В случае правильного ответа - выводить You are the winner.
#  Если за указанное количество попыток число не угадано - выводить: 'You are the loser' и правильное число.


from random import randint

start = int(randint(0, 50))
delta = int(randint(1, 50))
finish = start + delta
number = int(randint(start, finish))
print(str(f'Guess the number from {start} to {finish}'))

i = 5
print(str(f'You have {i} attempts'))

for j in range(1, i + 1):
    k = int(input('-->'))
    if k == number:
        print('You are the winner!!!')
        break
    else:
        ost = i - j
        if ost == 0:
            print('You are the loser...')
            print(f'Correct answer {number}')
        else:
            if k < number:
                print(str(f'You have {ost} attempts. Enter >'))
            if k > number:
                print(str(f'You have {ost} att. Enter <'))
