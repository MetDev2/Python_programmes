"""
Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется
для определения количества чисел, меньших n, которые взаимно просты с n.
К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с девятью, φ(9)=6.

n	Взаимно простые числа	φ(n)	n/φ(n)
2	1	                1	2
3	1,2	                2	1.5
4	1,3	                2	2
5	1,2,3,4	                4	1.25
6	1,5	                2	3
7	1,2,3,4,5,6	        6	1.1666...
8	1,3,5,7	                4       2
9	1,2,4,5,7,8	        6	1.5
10	1,3,7,9	                4	2.5
Нетрудно заметить, что максимум n/φ(n) наблюдается при n=6, для n ≤ 10.

Найдите значение n ≤ 1 000 000, при котором значение n/φ(n) максимально.
"""
def some_primes():
    a = list(range(100))
    a[1] = 0
    list_of_primes = [2]
    i = 3
    for j in range(2, 100, 2):
        a[j] = 0
    for i in range(100):
        if a[i] != 0:
            list_of_primes.append(a[i])
            for j in range(i**2, 100, i*2):
                a[j] = 0
    return list_of_primes

def totient_maximum(n):
    totient_max = 2
    i = 1
    prime = some_primes()
    while totient_max * prime[i] < n:
        totient_max *= prime[i]
        i += 1
    return totient_max
        



if __name__ == '__main__':
    print(totient_maximum(1000000))
