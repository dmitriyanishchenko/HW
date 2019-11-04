# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1

# # Option #1
list_old_1 = [1, 2, 3, 4, 5, 6, 7, 8]
first_elem_1 = list_old_1[0]
list_new_1 = []
i = 0
while i < len(list_old_1) - 1:
    elem = list_old_1[i + 1]
    list_new_1.append(elem)
    i += 1
list_new_1.append(first_elem_1)
print(list_old_1, '--->', list_new_1)

# Option #2
list_old_2 = [10, 11, 12, 13, 14, 15]
first_elem_2 = list_old_2[0]
list_new_2 = []
for el in range(len(list_old_2) - 1):
    el_new = list_old_2[el + 1]
    list_new_2.append(el_new)
list_new_2.append(first_elem_2)
print(list_old_2, '--->', list_new_2)
