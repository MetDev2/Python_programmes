"""Найдите сумму всех четных элементов ряда Фибоначчи,
которые не превышают четыре миллиона.
"""
def even_fib_num(max_num):
    summary = 0
    a = 1
    b = 2
    while b < max_num:
        a, b = b, a + b
        if a % 2 == 0:
            summary += a

    return summary



if __name__ == "__main__":
    print(even_fib_num(4*10**6))
