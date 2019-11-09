# Для каждого натурального числа в промежутке от m до n вывести все делители, кроме единицы и самого числа.
# m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
#
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35

m = int(input('Enter a positive integer m --->\t'))
n = int(input('Enter a positive integer n, more with number m --->\t'))

if n < m or m < 1 or n < 1:
    print('WRONG INPUT!')
else:
    matrix = []
    for i in range(m, n + 1):
        row = [i]
        for j in range(2, i):
            if i % j == 0:
                row.append(j)
        matrix.append(row)
        print(row)
