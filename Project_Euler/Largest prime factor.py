"""Каков самый большой делитель числа 600851475143,
являющийся простым числом?
"""
def largest_prime_factor(n):
    i = 2
    k = []
    while i * i <= n:
        while n % i == 0:
            k.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        k.append(n)
    return max(k)



if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
