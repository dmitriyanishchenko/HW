# Найти все пары дружественных чисел в промежутке от 200 до 300

for i in range(200, 300):
    summ = 0
    for j in range(1, i//2 + 1):
        if not i % j:
            summ = summ + j

    summ_del = 0
    for k in range(1, summ//2 + 1):
        if not summ % k:
            summ_del = summ_del + k

    if summ_del == i and summ != i:
        string = f'{str(i)} - {str(summ)}'
        print(string)
