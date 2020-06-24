"""Найдите самый большой палиндром,
полученный умножением двух трехзначных чисел."""
def largest_palindrome_product(lower_limit, upper_limit):
    k = []
    for i in range(lower_limit, upper_limit, 1):
        if i % 10 == 0:
            continue
        else:
            for j in range(i, upper_limit, 1):
                if j % 10 == 0:
                    continue
                else:
                    number = str(i*j)
                    if number == number[::-1]:
                        k.append(int(number))

    return max(k)



if __name__ == "__main__":
    print(largest_palindrome_product(100, 1000)) 
