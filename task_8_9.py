import math

def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


e = 2, 718  # число Эйлера, всегда постоянная величина(экспонента)


def sin1(x):
    n = 1
    sign = -1
    result = 0
    while True:
        sign *= -1
        term = x ** n / fact(n)
        term = sign * term
        result += term
        n += 2
        k = math.abs(term)
        if k <= e:
            break
    return result


k = sin1(90)
print(k)
