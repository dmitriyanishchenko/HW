# Ввести число, проверить на то, что было введено именно число. Возвести его в куб.

number = input('Enter  number--->\t')
if number.isdigit():
    cube = int(number) ** 3
    print(f'{number} ** 3 = {cube}')
else:
    print('Wrong input!')
