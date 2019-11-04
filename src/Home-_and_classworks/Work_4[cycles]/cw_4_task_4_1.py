# Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.

numbers_list = [2, 5, 7, 22, 33, 11, 3, 2]
summ_elem = 0
for elem in numbers_list:
    if elem > 10:
        summ_elem += elem
print(summ_elem)
