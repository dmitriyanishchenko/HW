# Создать список с фамилиями. Вывести все фамилии, которые начинаются на П и заканчиваются на а

list_lastnames = ['Иванов', 'Петрова', 'Сидоров', 'Прохорова']
for lastname in list_lastnames:
    if lastname[0] == 'П' and lastname[-1] == 'а':
        print(lastname)
