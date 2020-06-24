"""Начиная с вершины представленного ниже треугольника и переходя к прилежащим
числам в следующем ряду, максимальная возможная сумма пройденных чисел
по пути от вершины до основания равна 23.

3
7 4
2 4 6
8 5 9 3

Т.е., 3 + 7 + 4 + 9 = 23.

Найти максимальную сумму при переходе от вершины до основания треугольника,
представленного текстовым файлом triangle.txt,
в котором содержится треугольник с одной сотней строк.
"""
def path_sum(filename):
    triangle_list = []
    string_counter = -1
    with open(filename) as tri:
        for line in tri:
            string_counter += 1
            triangle_list.append(list(map(int, (line.strip()).split())))
    for i in range(string_counter, 0, -1):
        for j in range(i):
            triangle_list[i-1][j] += max(triangle_list[i][j],
                                         triangle_list[i][j+1])
    return triangle_list[0][0]



if __name__ == "__main__":
    print(path_sum('triangle.txt'))
