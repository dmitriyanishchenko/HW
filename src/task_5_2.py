# Для каждого натурального числа впромежутке от m до n
#  вывести все делители, кроме единицы и самого числа.
# m и n вводятся с клавиатуры

m = int(input('Enter m-->:'))
n = int(input('Enter n-->:'))

for i in range(m, n+1):
    row = [i]
    for j in range(2, i):
        if i%j == 0:
            row.append(j)
    print(row)

