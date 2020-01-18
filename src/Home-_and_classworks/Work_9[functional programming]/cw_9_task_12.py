# Дан словарь, создать новый словарь, поменяв местам ключ и значение

old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
new_dict = {value: key for key, value in old_dict.items()}
print(old_dict, '--->', new_dict)
