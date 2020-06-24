"""Используйте names.txt, текстовый файл размером 46 КБ, содержащий
более пяти тысяч имен. Начните с сортировки в алфавитном порядке. Затем
подсчитайте алфавитные значения каждого имени и умножьте это значение на
порядковый номер имени в отсортированном списке для получения количества
очков имени.

Какова сумма очков имен в файле?
"""
def names_scores(filename):
    summary = 0
    sum_ord = 0
    with open(filename) as names:
        a = names.read().strip('"')
    list_of_names = sorted(a.split('","'))
    for i, name in enumerate(list_of_names, 1):
        for char in name:
            sum_ord += ord(char) - 64
        summary += i * sum_ord
        sum_char = 0
    return summary



if __name__ == "__main__":
    print(names_scores("names.txt"))
