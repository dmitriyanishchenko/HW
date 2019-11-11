# Написать 12 функций по переводу:
# 1. Дюймы в сантиметры
# 2. Сантиметры в дюймы
# 3. Мили в километры
# 4. Километры в мили
# 5. Фунты в килограммы
# 6. Килограммы в фунты
# 7. Унции в граммы
# 8. Граммы в унции
# 9. Галлон в литры
# 10. Литры в галлоны
# 11. Пинты в литры
# 12. Литры в пинты
#
# Примечание: функция принимает на вход число и возвращает конвертированное число


def in_to_cm(trans_value):
    result = round(2.54 * trans_value, 4)
    return result


def cm_to_in(trans_value):
    result = round(trans_value * 0.3937, 4)
    return result


def mi_to_km(trans_value):
    result = round(trans_value * 1.60934, 4)
    return result


def km_to_mi(trans_value):
    result = round(trans_value * 0.621371192, 4)
    return result


def lb_to_kg(trans_value):
    result = round(trans_value * 0.45359237, 4)
    return result


def kg_to_lb(trans_value):
    result = (trans_value * 2.20462262, 4)
    return result


def oz_to_g(trans_value):
    result = round(trans_value * 28.3495231, 4)
    return result


def g_to_oz(trans_value):
    result = round(trans_value * 0.0352739619, 4)
    return result


def gal_to_l(trans_value):
    result = round(trans_value * 3.785411784, 4)
    return result


def l_to_gal(trans_value):
    result = round(trans_value * 0.264172052, 4)
    return result


def pint_to_l(trans_value):
    result = (trans_value * 0.56826125, 4)
    return result


def l_to_pint(trans_value):
    result = round(trans_value * 1.7597539863927, 4)
    return result


def main():
    print(
        ' 1. Inches to centimeters'
        '   2. Centimeters to inches\n'
        ' 3. Miles to kilometers'
        '     4. Kilometers to miles\n'
        ' 5. Pounds to kilograms'
        '     6. Kilograms to pounds\n'
        ' 7. Ounces to grams'
        '         8. Grams to ounce\n'
        ' 9. Gallon to liters'
        '       10. Liters to Gallons\n'
        '11. Pints to liters'
        '        12. Liters to pints\n'
    )
    num_func = input('Enter the numerical value of the translation function:--->\t')
    trans_value = input('Enter translatable value -->\t')
    if not num_func.isdigit() or not 1 <= int(num_func) <= 12 or not trans_value.isdigit() or int(trans_value) <= 0:
        print('Wrong input!!!')

    else:
        num_func = int(num_func)
        trans_value = float(trans_value)

        if num_func == 1:  # 1. Дюймы в сантиметры
            units = ['inches', 'centimeters']
            result = in_to_cm(trans_value)

        elif num_func == 2:  # 2. Сантиметры в дюймы
            units = ['centimeters', 'inches']
            result = cm_to_in(trans_value)

        elif num_func == 3:  # 3. Мили в километры
            units = ['miles', 'kilometers']
            result = mi_to_km(trans_value)

        elif num_func == 4:  # 4. Километры в мили
            units = ['kilometers', 'miles']
            result = km_to_mi(trans_value)

        elif num_func == 5:  # 5. Фунты в килограммы
            units = ['pounds', 'kilograms']
            result = lb_to_kg(trans_value)

        elif num_func == 6:  # 6. Килограммы в фунты
            units = ['kilograms', 'pounds']
            result = kg_to_lb(trans_value)

        elif num_func == 7:  # 7. Унции в граммы
            units = ['ounces', 'grams']
            result = oz_to_g(trans_value)

        elif num_func == 8:  # 8. Граммы в унции
            units = ['grams', 'ounces']
            result = g_to_oz(trans_value)

        elif num_func == 9:  # 9. Галлоны в литры
            units = ['gallon', 'liters']
            result = gal_to_l(trans_value)

        elif num_func == 10:  # 10. Литры в галлоны
            units = ['liters', 'gallon']
            result = l_to_gal(trans_value)

        elif num_func == 11:  # 11. Пинты(брит.) в литры
            units = ['pints', 'liters']
            result = pint_to_l(trans_value)

        else:
            units = ['liters', 'pints']
            result = l_to_pint(trans_value)

        print(f'In {trans_value} {units[0]} {result} {units[1]}')


if __name__ == '__main__':
    main()
