"""Какое самое маленькое число делится нацело на все числа от 1 до 20?"""
import math
def smallest_multiple(max_divisor):
    prime = [2]
    pow_ = 1
    multi = 0
    for i in range(3, max_divisor+1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        kor = int(math.sqrt(i))
        for j in prime:
            if i % j == 0:
                break
            if j >= kor:
                prime.append(i)
                break
    while 2 ** (pow_+1) < max_divisor:
        pow_ += 1
    multi = 2 ** pow_
    for i in prime[1::]:
        while i ** pow_ > max_divisor:
            pow_ -= 1
        multi *= i ** pow_

    return multi



if __name__ == "__main__":
    print(smallest_multiple(20))
