# Вычислить квадратное уравнение ax2 + bx + c = 0 (*)
# D = b2 – 4ac;
# x1,2 = (-b +/- sqrt (D)) / 2a
# Предусмотреть 3 варианта:
#      Два действительных корня
#      Один действительный корень
#      Нет действительных корней


print('Solve a quadratic equation of the form  ax2 + bx + c = 0')
a = float(input('Enter value  a --->'))
b = float(input('Enter value  b --->'))
c = float(input('Enter value  c --->'))
discriminant = b ** 2 - (4 * a * c)
print(f'discriminant is {discriminant}')
if discriminant < 0:
    print('No valid roots')
elif discriminant == 0:
    single_root = (-b) / 2 * a
    print(f'x = {single_root}')
else:
    root_1 = (- b + discriminant ** 0.5) / 2 * a
    root_2 = (- b - discriminant ** 0.5) / 2 * a
    print(f'x1 = {root_1}, x2 = {root_2}')
