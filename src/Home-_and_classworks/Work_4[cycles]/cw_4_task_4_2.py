# Просуммировать неопределенное количество чисел, вводимых пользователем, суммировать до тех пор,
# пока пользователь не введёт слово «стоп»

summ_numbers = 0
while True:
    number = input('Enter number for addition or "stop" for break --->')
    if number == 'stop':
        break
    summ_numbers += int(number)
print(f'Sum of entered numbers is {summ_numbers}')
