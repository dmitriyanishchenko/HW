# Ввести предложение. Если число символов в предложении
# кратно 3 - добавить ! к концу строки. Вывести строку на экран

some_sentence = input('Enter some sentence \t')
len_sentence = len(some_sentence)
if len_sentence % 3 == 0:
    some_sentence += '!'
print(some_sentence)
