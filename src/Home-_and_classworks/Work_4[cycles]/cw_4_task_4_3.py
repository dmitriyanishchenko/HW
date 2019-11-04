# Просуммировать неопределенное количество чисел, вводимых пользователем,
# суммировать до тех пор, пока пользователь не введёт слово «стоп». Не учитывать числа кратные 5

summ_numbers = 0
while True:
    number = input('Enter number for addition or "stop" for break --->')
    if number == 'stop':
        break
    elif not int(number) % 5 == 0:
        summ_numbers += int(number)
print(f'The sum of the entered numbers, except for multiples of 5, is {summ_numbers}')
