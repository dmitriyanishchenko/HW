# Составить список чисел Фибоначчи содержащий 15 элементов

#  Option #1
n = 13
i = 1
fib_line_1 = [0, 1]
while i < n + 1:
    elem = int(fib_line_1[i]) + int(fib_line_1[i - 1])
    fib_line_1.append(elem)
    i += 1
print(f'Fibonacci list {n + 2}! = {fib_line_1}')

# # # Option #2
n_2 = 13
fib_line_2 = [0, 1]
for i in range(2, n_2+2):
    elem = fib_line_2[i - 1] + (fib_line_2[i - 2])
    fib_line_2.append(elem)
print(f'Fibonacci list {n_2 + 2}! = {fib_line_2}')
