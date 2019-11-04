# Дан список целых чисел. Подсчитать сколько четных чисел в списке

# Option #1
list_old_1 = [1, 2, 3, 4, 5, 6]
counter_1 = 0
i = 0
while i < len(list_old_1):
    if list_old_1[i] % 2 == 0:
        counter_1 += 1
    i += 1
print(f'In the list {list_old_1} {counter_1} even numbers')

# Option #2
list_old_2 = [3, 61, -8, -1, 22, 13]
counter_2 = 0
for elem in list_old_2:
    if elem % 2 == 0:
        counter_2 += 1
print(f'In the list {list_old_2} {counter_2} even numbers')
