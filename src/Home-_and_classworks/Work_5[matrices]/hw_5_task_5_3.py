# Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
# Вычислить результат Z в зависимости от знака. Предусмотреть реакции на возможный неверный знак операции,
# а также на ввод Y=0 при делении. Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл). В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0')

sure_sign = ['+', '-', '*', '/', '0']
while True:
    x = input('Enter number X -->\t')
    y = input('Enter number Y -->\t')
    sign = input('Enter + - * / or 0=stop\t')
    if sign == '0':
        break
    if not x.isdigit() or not y.isdigit() or sign not in sure_sign:
        print('Wrong input!')
        continue
    else:
        x = int(x)
        y = int(y)
        if y == 0 and sign == '/':
            print('Cannot be divided by zero!')
            continue
        else:
            if sign == '+':
                result = x + y
            elif sign == "-":
                result = x - y
            elif sign == '*':
                result = x * y
            elif sign == '/':
                result = x / y
            print(f'{x} {sign} {y} = {result}')
