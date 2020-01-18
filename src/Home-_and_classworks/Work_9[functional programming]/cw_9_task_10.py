# генератор словарей. Дан словарь, создать новый, добавив к ключам значения их длинн

old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
new_dict = {key + str(len(key)): value for key, value in old_dict.items()}
print(old_dict, '--->', new_dict)
