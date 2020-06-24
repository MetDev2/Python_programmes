"""Тройка Пифагора - три натуральных числа a < b < c,
для которых выполняется равенство a**2 + b**2 = c**2
Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
"""
def pythagorean_triplet(sum_of_abc):
    m = 2
    n = 1
    a = 1
    b = 1
    c = 1
    k = 1
    while sum_of_abc % (a+b+c) != 0:
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        k = sum_of_abc / (a+b+c)
        n += 1
        if n == m:
            m += 1
            n = 1
    a, b = min(a, b), max(a, b)
    a *= k
    b *= k
    c *= k
    return a * b * c



if __name__ == "__main__":
    print(pythagorean_triplet(1000))
