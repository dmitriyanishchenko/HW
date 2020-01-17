# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.

list_a = ['dog', 'cat', 'rat']
list_b = [f'{i} - {elem}' for i, elem in enumerate(list_a)]
print(list_b)
