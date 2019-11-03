# Получить на ввод количество рублей и копеек и вывести в правильной форме,
# например, 3 рубля, 1 рубль 25 копеек, 3 копейки

rubles = input('Enter the number of rubles --->')
cents = input('Enter the number of cents  --->')

if rubles.isdigit() and int(rubles) >= 0 and cents.isdigit() and 0 <= int(cents) < 100:
    rubles_int = int(rubles)
    cents_int = int(cents)

    root_rubles = 'рубл'  # корень в рублях
    root_cents = 'копе'  # корень в копейках

    if rubles_int == 1 or (21 <= rubles_int and rubles_int % 10 == 1):
        ending_rubles = 'ь'
    elif 2 <= rubles_int <= 4 or (22 <= rubles_int and 2 <= rubles_int % 10 <= 4):
        ending_rubles = 'я'
    else:
        ending_rubles = 'ей'

    if cents_int == 1 or (21 <= cents_int and cents_int % 10 == 1):
        ending_cents = 'йка'
    elif 2 <= cents_int <= 4 or (22 <= cents_int and 2 <= cents_int % 10 <= 4):
        ending_cents = 'йки'
    else:
        ending_cents = 'ек'

    print(f'{rubles} {root_rubles}{ending_rubles} {cents} {root_cents}{ending_cents}')

else:
    print('WRONG INPUT!')
