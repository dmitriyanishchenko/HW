# Для заданного числа N составить программу вычисления суммы
# S =  1 + 1/2 + 1/3 + 1/4 + ... + 1/N, где N - натуральное число
n = int(input('enter n-->'))
summ = 0

for i in range(1, n + 1):
    summ = summ + (1 / i)

print(summ)