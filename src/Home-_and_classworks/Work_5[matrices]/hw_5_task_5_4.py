# Дано число. Найти сумму и произведение его цифр.

sum_of_digits = 0
product_of_numbers = 1
number = input('Enter number > 10  --->')

if not number.isdigit() or int(number) < 10:
    print('Wrong input!')
else:
    for elem in number:
        elem = int(elem)
        sum_of_digits += elem
        product_of_numbers *= elem
    print(f'Sum of digits in number {number} is', sum_of_digits)
    print(f'Product of digits in number {number} is', product_of_numbers)

