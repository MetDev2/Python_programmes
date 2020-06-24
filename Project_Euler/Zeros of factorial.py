"""Найти, на сколько нулей заканчивается n!. n <= 1000"""
def null_factorial(n):
    a = 0
    i = 1
    while 5 ** i <= n:
        a += int(n / 5**i)
        i += 1
    return a



n = 25
k = null_factorial(n)
print(k)
