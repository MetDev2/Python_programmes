"Какое число является 10001-ым простым числом?"
import math
def n_prime(n):
    prime_list = [2]
    counter = 1
    number_to_check = 1
    while counter != n:
        number_to_check += 2
        if (number_to_check > 10) and (number_to_check % 10 == 5):
            continue
        kor = int(math.sqrt(number_to_check))
        for j in prime_list:
            if number_to_check % j == 0:
                break
            if j >= kor:
                counter += 1
                prime_list.append(number_to_check)
                break

    return prime_list[counter-1]



if __name__ == "__main__":
    print(n_prime(10001))
