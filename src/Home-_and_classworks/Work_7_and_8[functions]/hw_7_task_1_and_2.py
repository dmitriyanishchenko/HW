# Написать 12 функций по переводу:
# Дюймы в сантиметры
# Сантиметры в дюймы
# Мили в километры
# Километры в мили
# Фунты в килограммы
# Килограммы в фунты
# Унции в граммы
# Граммы в унции
# Галлон в литры
# Литры в галлоны
# Пинты в литры
# Литры в пинты
#
# Примечание: функция принимает на вход число и возвращает конвертированное число
#
# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на выбор 12 вариантов
# перевода(описанных в первой задаче). Пользователь вводит цифру от одного до двенадцати. После программа
# запрашивает ввести численное значение. Затем программа выдает конвертированный результат.
# Использовать функции из первого задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.


def in_to_cm(enter_value):
    """
    This function takes the distance in centimeters as input and converts it to inches
    """
    translation_result = round(2.54 * enter_value, 4)
    return translation_result


def cm_to_in(enter_value):
    """
    This function takes the distance in inches as input and converts them to centimeters
    """
    translation_result = round(enter_value / 2.54, 4)
    return translation_result


def mi_to_km(enter_value):
    """
    This function takes the distance in miles as input and converts it into kilometers
    """
    translation_result = round(enter_value * 1.60934, 4)
    return translation_result


def km_to_mi(enter_value):
    """
    This function takes the distance in kilometers as input and converts it into miles
    """
    translation_result = round(enter_value / 1.60934, 4)
    return translation_result


def lb_to_kg(enter_value):
    """
    This function takes mass in pounds as input and converts them to kilograms
    """
    translation_result = round(enter_value * 0.45359237, 4)
    return translation_result


def kg_to_lb(enter_value):
    """
    This function takes mass in kilograms as input and converts them to pounds
    """
    translation_result = (enter_value / 0.45359237, 4)
    return translation_result


def oz_to_g(enter_value):
    """
    This function takes as an input mass in ounces and converts them to grams
    """
    translation_result = round(enter_value * 28.3495231, 4)
    return translation_result


def g_to_oz(enter_value):
    """
    This function accepts mass in grams as input and converts them to ounces
    """
    translation_result = round(enter_value / 28.3495231, 4)
    return translation_result


def gal_to_l(enter_value):
    """
    This function takes the volume in gallons as input and converts them to liters
    """
    translation_result = round(enter_value * 3.785411784, 4)
    return translation_result


def l_to_gal(enter_value):
    """
    This function accepts the volume in liters as input and converts them to gallons
    """
    translation_result = round(enter_value / 3.785411784, 4)
    return translation_result


def pint_to_l(enter_value):
    """
    This function accepts the volume in pints as input and converts them to liters
    """
    translation_result = round(enter_value / 2.113, 4)
    return translation_result


def l_to_pint(enter_value):
    """
    This function accepts the volume in liters as input and converts them to pints
    """
    translation_result = round(enter_value * 2.113, 4)
    return translation_result


while True:
    num_func = input('Enter the numerical value of the translation function or 0 to quit:\n'

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
                     ' \t\t\t\t\t\t --->\t')

    if num_func == '0':
        print('Goodbye...')
        break
    if not num_func.isdigit() or not 0 < int(num_func) <= 12:
        print('Wrong input!!!')
        print('Be careful...')
        print('_' * 70)
        continue

    enter_value = input('Enter translatable value --->\t')

    valid_characters = '0123456789.'
    for elem in enter_value:
        if elem not in valid_characters:
            print('The entered value is not a number.... Repeat enter ')
            print('_' * 70)
            continue
    if float(enter_value) <= 0:
        print('Enter a positive value')
        print('_' * 70)
        continue
    else:

        num_func = int(num_func)
        enter_value = float(enter_value)

        if num_func == 1:  # 1. Дюймы в сантиметры
            units = ['inches', 'centimeters']
            result = in_to_cm(enter_value)

        elif num_func == 2:  # 2. Сантиметры в дюймы
            units = ['centimeters', 'inches']
            result = cm_to_in(enter_value)

        elif num_func == 3:  # 3. Мили в километры
            units = ['miles', 'kilometers']
            result = mi_to_km(enter_value)

        elif num_func == 4:  # 4. Километры в мили
            units = ['kilometers', 'miles']
            result = km_to_mi(enter_value)

        elif num_func == 5:  # 5. Фунты в килограммы
            units = ['pounds', 'kilograms']
            result = lb_to_kg(enter_value)

        elif num_func == 6:  # 6. Килограммы в фунты
            units = ['kilograms', 'pounds']
            result = kg_to_lb(enter_value)

        elif num_func == 7:  # 7. Унции в граммы
            units = ['ounces', 'grams']
            result = oz_to_g(enter_value)

        elif num_func == 8:  # 8. Граммы в унции
            units = ['grams', 'ounces']
            result = g_to_oz(enter_value)

        elif num_func == 9:  # 9. Галлоны в литры
            units = ['gallon', 'liters']
            result = gal_to_l(enter_value)

        elif num_func == 10:  # 10. Литры в галлоны
            units = ['liters', 'gallon']
            result = l_to_gal(enter_value)

        elif num_func == 11:  # 11. Пинты(брит.) в литры
            units = ['pints', 'liters']
            result = pint_to_l(enter_value)

        else:
            units = ['liters', 'pints']
            result = l_to_pint(enter_value)

        print(f'In {enter_value} {units[0]} {result} {units[1]}')
        print('_' * 70)
