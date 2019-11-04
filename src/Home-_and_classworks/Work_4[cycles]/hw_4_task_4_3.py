# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()

# Option 1
dict_opt_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys_list_1 = list(dict_opt_1.keys())
i = 0
while i < len(keys_list_1):
    key1 = keys_list_1[i]
    l_key = len(keys_list_1[i])
    new_key = f'{key1}{l_key}'
    dict_opt_1[new_key] = dict_opt_1.pop(key1)
    i += 1
print(dict_opt_1)


# Option 2
dict_opt_2 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys_list_2 = list(dict_opt_2.keys())
for old_key in keys_list_2:
    len_key = len(old_key)
    new_key = f'{old_key}{len_key}'
    dict_opt_2[new_key] = dict_opt_2.pop(old_key)
print(dict_opt_2)
