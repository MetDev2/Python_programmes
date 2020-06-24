"""Найдите наибольшее произведение тринадцати
последовательных цифр в числе из файла number.txt.
"""
def largest_product(filename, n):
    max_product = 0
    product = 1
    number = ''
    a = ''
    with open(filename) as num:
        for line in num:
            a += line.strip()
    list_of_numbers = list(filter(lambda x: len(x) >= n, a.split('0')))
    for i in range(len(list_of_numbers)):
        number = list_of_numbers[i]
        for j in range(n):
            product *= int(number[j])
        if product > max_product:
            max_product = product
        for k in range(len(number))[n::]:
            product = product / int(number[k-n])
            product = product * int(number[k])
            if product > max_product:
                max_product = product
        product = 1

    return max_product



if __name__ == "__main__":
    print(largest_product('number.txt', 13))


