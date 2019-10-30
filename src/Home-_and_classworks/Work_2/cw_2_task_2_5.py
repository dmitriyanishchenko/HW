# 1. Создать два списка произвольного содержания.
# 2. Добавить к каждому списку по одному элементу:
#       а. в конец;
#       b. в начало.
# 3. Расширить первый список вторым.
# Все изменения выводить на экран.

listing_1 = [113, ['python', 'pycharm'], 45.3]
listing_2 = [(2.5, 8, 'c'), 'java', {'TMS_student': 'Ivan'}]
print('1. ', listing_1, '<----------------->', listing_2)

start_elem = 'abc'
finish_elem = 'def'
listing_1.insert(0, start_elem)
listing_2.insert(0, start_elem)
print('2. ', listing_1, '<---------->', listing_2)

len_listing_1 = len(listing_1)
len_listing_2 = len(listing_2)
listing_1.insert(len_listing_1, finish_elem)
listing_2.insert(len_listing_2, finish_elem)
print('   ', listing_1, '<--->', listing_2)

listing_1.extend(listing_2)
print('4. ', listing_1)
