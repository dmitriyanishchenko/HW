# Создать список учеников подобной структуры.
# Определить средний балл оценок по всем предметам, и вывести сведения
# о студентах, средний балл которых больше 4.

pupils = [
    {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Oleg',
        'Group': 42,
        'physics': 4,
        'informatics': 8,
        'history': 4,
    },
    {
        'firstname': 'Denis',
        'Group': 42,
        'physics': 3,
        'informatics': 4,
        'history': 3,
    },
]
summ_phy = 0
summ_inf = 0
summ_his = 0

good_pupils = []

for pupil in pupils:
    summ_phy += pupil['physics']
    summ_inf += pupil['informatics']
    summ_his += pupil['history']
    if (pupil['physics'] + pupil['informatics'] + pupil['history']) / 3 > 4:
        good_pupils.append(pupil)

for pupil in good_pupils:
    print(f'{pupil["firstname"]} is good')


amount_of_pupils = len(pupils)
mean_phy = round(summ_phy / amount_of_pupils, 2)
mean_inf = round(summ_inf / amount_of_pupils, 2)
mean_his = round(summ_his / amount_of_pupils, 2)

print(f'mean for physics is {mean_phy}')
print(f'mean for informatics is {mean_inf}')
print(f'mean for history {mean_his}')
