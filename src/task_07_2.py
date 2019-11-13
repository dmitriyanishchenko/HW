    # Написать программу со следующим интерфейсом: пользователю предоставляется на выбор 12 вариантов
    # перевода(описанных в задаче  7_1). Пользователь вводит цифру от 1 до 12. После программа запрашивает
    # ввести численное значение. Затем программа выдает конверитрованный результат. Использовать функции из первого задания.
    # ПРограмма должна быть в бесконечном цикле. Код выхода из программы - "0"

def in_to_cm(value):  # 1. Дюймы в сантиметры
    result = 2.54 * value
    return result

def cm_to_in(value):  # 2. Сантиметры в дюймы
    result = 0.393700787 * value
    return result

def mi_to_km(value):  # 3. Мили в километры
    result = 1.60934 * value
    return result

def km_to_mi(value):  # 4. Километры в мили
    result = 0.621371192 * value
    return result

def lb_to_kg(value):  # 5. Фунты в килограммы
    result = 0.45359237 * value
    return result

def kg_to_lb(value):  # 6. Килограммы в фунты
    result = 2.20462262 * value
    return result

def oz_to_g(value):  # 7. Унции в граммы
    result = 28.3495231 * value
    return result

def g_to_oz(value):  # 8. Граммы в унции
    result = 0.0352739619 * value
    return result

def gal_to_l(value):  # 9. Галлоны в литры
    result = 3.785411784 * value
    return result

def l_to_gal(value):  # 10. Литры в галлоны
    result = 0.264172052 * value
    return result

def pint_to_l(value):  # 11. Пинты(Брит.) в литры
    result = 0.56826125 * value
    return result

def l_to_pint(value):  # 12. Литры в пинт(Брит.)
    result = 1.7597539863927 * value
    return result

while True:

    list_operation = [[' 1. Inches to centimeters'],
                      [' 2. Centimeters to inches'],
                      [' 3. Miles to kilometers'],
                      [' 4. Kilometers to miles'],
                      [' 5. Pounds to kilograms'],
                      [' 6. Kilograms to pounds'],
                      [' 7. Ounces to grams'],
                      [' 8. Grams to ounces'],
                      [' 9. Gallons to liters'],
                      ['10. Liters to gallons'],
                      ['11. Pints to liters'],
                      ['12. Liters to pints']]

    for row in list_operation:
        for elem in row:
            print(elem)

    number_operation = int(input('Enter number operation from 1 to 12 or 0 to quit -->'))
    if number_operation == 0:
        break
    valid_operation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    value = int(input('Enter value -->'))

    if number_operation not in valid_operation:
        print('Enter valid operations!')
        continue

    elif number_operation == 1:
        convert = in_to_cm(value)
        sim_1 = 'in'
        sim_2 = 'cm'
    elif number_operation == 2:
        convert = cm_to_in(value)
        sim_1 = 'cm'
        sim_2 = 'in'
    elif number_operation == 3:
        convert = mi_to_km(value)
        sim_1 = 'mi'
        sim_2 = 'km'
    elif number_operation == 4:
        convert = km_to_mi(value)
        sim_1 = 'km'
        sim_2 = 'mi'
    elif number_operation == 5:
        convert = lb_to_kg(value)
        sim_1 = 'lb'
        sim_2 = 'kg'
    elif number_operation == 6:
        convert = kg_to_lb(value)
        sim_1 = 'kg'
        sim_2 = 'lb'
    elif number_operation == 7:
        convert = oz_to_g(value)
        sim_1 = 'oz'
        sim_2 = 'g'
    elif number_operation == 8:
        convert = g_to_oz(value)
        sim_1 = 'g'
        sim_2 = 'oz'
    elif number_operation == 9:
        convert = gal_to_l(value)
        sim_1 = 'gal'
        sim_2 = 'l'
    elif number_operation == 10:
        convert = l_to_gal(value)
        sim_1 = 'l'
        sim_2 = 'gal'
    elif number_operation == 11:
        convert = pint_to_l(value)
        sim_1 = 'pint'
        sim_2 = 'l'
    else:
        convert = l_to_pint(value)
        sim_1 = 'l'
        sim_2 = 'pint'
    print(f'{value} {sim_1} = {convert} {sim_2}')
