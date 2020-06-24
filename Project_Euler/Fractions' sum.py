"""Даны две рациональные дроби: a/b и c/d. Сложить их и результат
представить в виде несократимой дроби m/n. Вывести числа m и n.
a, b, c, d <= 1000
"""
def frations_sum(a, b, c, d):
    if b == 0 or d == 0:
        print('На ноль делить нельзя')
        return False
    m, n = a*d + c*b, b*d
    if m == 0:
        return m, n
    if m == n:
        m, n = 1, 1
        return m, n
    znak = 1
    if m*n < 0:
        znak = -1
    m, n = abs(m), abs(n)
    for i in range(max(m, n), 1, -1):
        if m % i == 0 and n % i == 0:
            m /= i
            n /= i
            return m*znak, n



if __name__ == "__main__":
    print(frations_sum(3, 10, 5, 18))
