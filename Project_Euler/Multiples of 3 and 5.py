"""Найдите сумму всех чисел меньше 1000, кратных 3 или 5."""
def sum_of_muliples(upper_limit):
    summary = 0
    for i in range(3, upper_limit, 3):
        summary += i
        
    for j in range(5, 1000, 5):
        if j % 3 != 0: summary += j

    return summary



if __name__ == "__main__":
    print(sum_of_muliples(1000))
