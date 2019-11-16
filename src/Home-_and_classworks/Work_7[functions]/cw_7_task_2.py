# Написать программу для нахождения факториала.
#  Факториал натурального числа n определяется как
# произведение всех натуральных чисел от 1 до n включительно


while True:
    n = input('Enter natural number to find its factorial, or press <0> to STOP--->')
    if n == '0':
        print('Goodbye ;-)')
        break
    elif not n.isdigit() or int(n) < 1:
        print('Wrong input!!!')
        print('Repeat once again...')
        continue

    else:
        n = int(n)

        def factor(n):
            res = 1
            for elem in range(1, n+1):
                res *= elem
            return res


        print(f'{n}! = {factor(n)}')
