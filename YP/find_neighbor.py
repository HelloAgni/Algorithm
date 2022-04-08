import sys


def neighbor(table, coord_n, coord_m):
    """
    Написать функцию, которая для элемента возвращает всех его соседей.
    Соседним считается элемент, находящийся от текущего на одну ячейку влево,
    вправо, вверх или вниз. Диагональные элементы соседними не считаются.
    Элементы матрицы — целые числа, по модулю не превосходящие 1000.
    """
    table = [
        [1111]*(m+1)] + [
            list(map(int, i.split())) for i in table
        ] + [[1111]*(m+1)]
    # table = [[int(y) for y in ''.join(x).split()] for x in table]
    numbers = [table[coord_n+1][coord_m], table[coord_n-1][coord_m],
               table[coord_n][coord_m+1], table[coord_n][coord_m-1]]
    numbers = [x for x in numbers if x != 1111]
    numbers.sort()
    return numbers


if __name__ == '__main__':
    n = int(input())  # строки
    m = int(input())  # столбцы
    table = []
    for _ in range(n):
        line = '1111' + ' ' + sys.stdin.readline().rstrip() + ' ' + '1111'
        table.append(line)
    coord_n = int(input()) + 1  # строки c 0
    coord_m = int(input()) + 1  # столбцы c 0
    numbers = neighbor(table, coord_n, coord_m)
    print(*numbers)
