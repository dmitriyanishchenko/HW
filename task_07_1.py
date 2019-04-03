# Написать 12 функций по переводу:
# 1. Дюймы в сантиметры
# 2. Сантиметры в дюймы
# 3. Мили в километры
# 4. Километры в мили
# 5. Фунты в килограммы
# 6. Килограммы в фунты
# 7. Унции в граммы
# 8. Граммы в унции
# 9. Галлоны в литры
# 10. Литры в галлоны
# 11. Пинты в литры
# 12. Литры в пинты

value = int(input('Enter value -->'))

def in_to_cm(value): # 1. Дюймы в сантиметры
    result = 2.54 * value
    return result

def cm_to_in(value): #2. Сантиметры в дюймы
    result = 0.393700787 * value
    return result

def mi_to_km(value): # 3. Мили в километры
    result = 1.60934 * value
    return result

def km_to_mi(value): # 4. Километры в мили
    result = 0.621371192 * value
    return result

def lb_to_kg(value): # 5. Фунты в килограммы
    result = 0.45359237 * value
    return result

def kg_to_lb(value): # 6. Килограммы в фунты
    result = 2.20462262 * value
    return result

def oz_to_g(value): # 7. Унции в граммы
    result = 28.3495231 * value
    return result

def g_to_oz(value): # 8. Граммы в унции
    result = 0.0352739619 * value
    return result

def gal_to_l(value): # 9. Галлоны в литры
    result = 3.785411784 * value
    return result

def l_to_gal(value): # 10. Литры в галлоны
    result = 0.264172052 * value
    return result

def pint_to_l(value): # 11. Пинты(брит.) в литры
    result = 0.56826125 * value
    return result

def l_to_pint(value): # 12. Литры в пинты(брит.)
    result = 1.7597539863927 * value
    return result
