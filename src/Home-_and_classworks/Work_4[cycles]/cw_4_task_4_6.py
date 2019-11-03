# Получить сумму кубов натуральных чисел от n до m используя цикл for

n = int(input('Enter positive integer number n ---> '))
m = int(input('Enter positive integer number m, greater than n ---> '))
if n < 0 or m < 0 or n > m:
    print('Wrong input!')
else:
    sum_cube = 0
    for elem in range(n, m + 1):
        sum_cube += elem ** 3
    print(f'The sum of the cubes of natural numbers from {n} to {m} is {sum_cube}')
