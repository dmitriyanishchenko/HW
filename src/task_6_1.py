# Написать программу, в которой вводятся два
# операнда X и Y и знак операции (+ - * /)
# вычисить результат в зависимости от знака.
# предусмотреть реакции на неверный знак операции
# а также на ввод 0 при делении
i = 5
sure_sign = ['+', '-', '*', '/', '0']
while i > 0:

    x = int(input('Enter number X -->'))
    y = int(input('Enter number Y -->'))
    sign = input('Enter + - * / or 0=stop')

    if y == 0 and sign == '/':
        print('На ноль делить нельзя!!!')
        continue

    if sign in sure_sign:
        if sign == '0':
            break
        elif sign == '+':
            result = x + y
        elif sign == "-":
            result = x - y
        elif sign == '*':
            result = x * y
        elif sign == '/':
            result = x / y
        print(result)
    else:
        print('Неверный знак операции!!!')
