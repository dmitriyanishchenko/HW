# генератор списков

list_a = [i for i in range(5)]
print(list_a)

# Дан список слов. Сгенерировать новый список с перевернутыми словами

list_a = ['word', 'papa', 'mama']
list_b = [word[::-1] for word in list_a]
print(list_a, '--->', list_b)
