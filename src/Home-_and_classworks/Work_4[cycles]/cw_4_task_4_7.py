# Ввести два целых числа A и B ( A < B ).
# Вывести в порядке возрастания все целые числа, расположенные между A и B
# (включая сами числа A и B ), а также количество N этих чисел.

num_a = int(input('Enter integer number A ---> '))
num_b = int(input('Enter integer number B, greater than A ---> '))
if num_b < num_a:
    print('Wrong input!')
else:
    count = 0
    for elem in range(num_a, num_b + 1):
        print(elem)
        count += 1
    print(f'{count} numbers')
