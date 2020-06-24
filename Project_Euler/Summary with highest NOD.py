"""Дано натурально число n.Представить n в виде a + b,
так, что НОД(a, b) максимален, a <= b. Вывести a и b.
Если возможно несколько ответов - вывести ответ с минимальным a. n <= 10**7
"""
def decompose(n):
    a, b = 0, n
    i = 2
    NOD = 1
    c = 1
    while i * i <= n:
        while n % i == 0:
            if c == 1:
                c = i
            else:
                NOD *= i
            n = n / i
        i = i + 1
    if n > 1:
        NOD *= n
    if c == 1:
        print("Вы ввели простое число или 1")
        return a, b
    a, b = NOD, NOD*(c-1)
    return a, b



if __name__ == "__main__":
    print(decompose(13))
