#  Дан список словарей. Каждый словарь описывает машину(серийный номер и год выпуска).
#  Создать новый список со всеми машинами, год выпуска которых больше n

list_car = [

    dict(number='01', year=1996),
    dict(number='02', year=1997),
    dict(number='03', year=1998),
    dict(number='04', year=1999),
    dict(number='05', year=2000)

]

list_car_2 = [car for car in list_car if car['year'] > 1998]
print(list_car_2)
