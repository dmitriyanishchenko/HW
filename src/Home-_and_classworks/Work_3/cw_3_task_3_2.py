#   ФОРМАТИРОВАНИЕ СТРОК
# firstname = input('Input your firstname: ')
# lastname = input('Input your lastname: ')
#
# string_a = 'Hello, %s %s' % (firstname, lastname)
# string_b = 'Hello, {} {}'.format(firstname, lastname)
# string_c = 'Hello, {0} {1}'.format(firstname, lastname)
# string_d = f'Hello, {firstname} {lastname}'

# Запросить у пользователя два целых числа.
# Вывести строку вида “2 плюс 3 равно 5”
# Примечание: после ввода переменных преобразовать переменные к типу int
#  >> first_number = int(first_number)

integer_number_1 = int(input('Enter first integer number:'))
integer_number_2 = int(input('Enter second integer number:'))
summ_of_variables = integer_number_1 + integer_number_2
print(f'{integer_number_1} add {integer_number_2} equally {summ_of_variables}')
