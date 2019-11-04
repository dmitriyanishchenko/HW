# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых
# чисел от 1 до n(включая n) используя цикл while

n = int(input('Enter the value of number "n" --->\t'))
sum_of_cube = 0
counter = 1
while counter <= n:
    sum_of_cube += counter ** 3
    counter += 1
print(f"The sum of the cubes of all integers numbers from 1 to {n} is {sum_of_cube}")
