"""Найдите разность между суммой квадратов
и квадратом суммы первых ста натуральных чисел."""
def sum_square_difference(n):
    result = 0
    sum1 = 0
    sum2 = 0
    for i in range(1, n+1):
        sum1 += i**2
        sum2 += i
    sum2 = sum2 ** 2
    result = sum2 - sum1

    return result



if __name__ == "__main__":
    print(sum_square_difference(100))
