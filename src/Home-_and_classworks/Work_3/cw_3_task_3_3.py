# Дополнительные функции по работе со строками
#
# string = 'Hello,_my_name_is_Alex'
# print(string)
#
# string_list = string.split('_')
# print(string_list)
#
# result = '  '.join(string_list)
# print(result)
#
# string = 'ping pong'
# print(string)
#
# result_string = string.replace('p', 'k')
# print(result_string)

# Ввести предложение состоящее из двух слов.
# Поменять местами слова, добавить восклицательный знак в начало и конец,
# вывести итоговое предложение на экран.

start_sentence = input('enter a two-line sentence: ')
split_sentence = start_sentence.split(' ')
result_sentence = '!{1} {0}!'.format(split_sentence[0], split_sentence[1])
print(result_sentence)
