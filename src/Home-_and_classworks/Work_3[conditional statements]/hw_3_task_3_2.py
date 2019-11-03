# В семье N свадьба. Они решили выбрать заведение, где будут праздновать в зависимости от
# количества людей, которое прибудет к утру.
# Если их будет больше 50 - закажут ресторан, если от 20 до 50 -то кафе, а если меньше 20 то отпраздную дома.
# Вывести "ресторан", "кафе", "дом" в зависимости от количества гостей (прочитать переменную с консоли)

number_of_guests = input('Enter number of guests --->')

if not number_of_guests.isdigit() or int(number_of_guests) < 1:
    print('Wrong input!')
else:
    int_number_of_guests = int(number_of_guests)
    if int_number_of_guests < 20:
        place = 'Home'
    elif int_number_of_guests > 50:
        place = 'Restaurant'
    else:
        place = 'Cafe'
    print(f'Celebrate the wedding in {place}')
