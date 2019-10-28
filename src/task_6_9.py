from datetime import datetime
trains = [
{
            'number': '026B',
            'from' : 'Minsk',
            'to': 'Moscow',
            'departure': 'datetime(2019, 4, 2, 19, 24)',
            'arrival': 'datetime(2019, 4, 3, 5, 29)'
            },
{
            'number': '086B',
            'from': 'Minsk',
            'to': 'Kiev',
            'departure': 'datetime(2019, 4, 4, 22, 40)',
            'arrival': 'datetime(2019, 4, 5, 8, 59)'
            },   {
            'number': '708B',
            'from': 'Minsk',
            'to': 'Gomel',
            'departure': 'datetime(2019, 4, 2, 19, 00)',
            'arrival': 'datetime(2019, 4, 2, 21, 54)'
            },
]
print(str(trains))
for train in trains:
    #вычислить время в пути = прибытие - отправление
        #если время в пути  больше 7.20:

        for key, value in train.items():
            print(f'{key}: {value}')
        print('*************')
