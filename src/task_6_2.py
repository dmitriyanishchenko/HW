#Дано число, найти сумму и произведение его цифр

summ = 0
mult = 1
number = input('Enter number > 10  --->')
num_list = list(number)

for elem in num_list:
    elem = int(elem)
    summ += elem
    mult *= elem

print(f'Sum of numbers =', summ)
print(f'Product of numbers =', mult)

