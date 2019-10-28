# Все начальные данные задаются произвольно.
# Задачи по обработке чисел :
#
#   1. Даны 2 действительных числа a и b. Получить их сумму, разность и произведение.
#   2. Даны действительные числа x и y. Получить (|x|- |y|)  / (1+ |xy|)
#   3. Дана длина ребра куба. Найти объем куба и площадь его боковой поверхности.
#   4. Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел
#   5. Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.


# 1.
a = int(input('Enter first number:\t'))
b = int(input('Enter second number:'))
result_addition = a + b
result_subtraction = a - b
result_division = a / b
print(f'Result addition {a} and {b} is {result_addition}')
print(f'Result subtraction {a} and {b} is {result_subtraction}')
print(f'Result division {a} and {b} is {result_division}')

# 2.
x = float(input('Enter number X:\t'))
y = float(input('Enter number Y:\t'))
result = (abs(x) - abs(y)) / (1 + abs(x * y))
print(result)

# 3.
cube_edge = float(input('Enter the length of the cube edge: '))
cube_volume = round(cube_edge ** 3, 3)
cube_surface_area = round(cube_edge ** 2 * 6, 3)
print(f'Cube volume is {cube_volume} cubic meters; cube surface area is {cube_surface_area} square meters.')

# 4.
c = float(input('Enter number C:\t'))
d = float(input('Enter number D:\t'))
arithmetic_mean = (c + d) / 2
geometric_mean = round((c * d) ** 0.5, 3)
print(f'Arithmetic mean of numbers {c} and {d} is {arithmetic_mean}, geometric mean of these numbers '
      f'is {geometric_mean}')

# 5.
print('Enter the length of the legs of a right-angled triangle:')
side_b = float(input('1. '))
side_c = float(input('2. '))
hypotenuse = round((side_b ** 2 + side_c ** 2) ** 0.5, 3)
print(f'The length of the hypotenuse of a right triangle with the length of legs {side_b} and {side_c} is {hypotenuse}')
