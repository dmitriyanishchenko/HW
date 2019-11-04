# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному
# элементу умноженному на -2

# Option #1
list_old_1 = [23, -7, 2, 6, 67, 10]
list_new_1 = []
i = 0
while i < len(list_old_1):
    elem = int(list_old_1[i]) * -2
    list_new_1.append(elem)
    i += 1
print(list_old_1, '--->', list_new_1)

# Option #2
list_old_2 = [3, 61, -8, 52, 4, 13]
list_new_2 = []
for elem in list_old_2:
    elem_new = elem * (-2)
    list_new_2.append(elem_new)
print(list_old_2, '--->', list_new_2)
