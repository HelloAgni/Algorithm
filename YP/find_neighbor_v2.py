def neighbor(table, coord_n, coord_m):
    """
    Написать функцию, которая для элемента возвращает всех его соседей.
    Соседним считается элемент, находящийся от текущего на одну ячейку влево,
    вправо, вверх или вниз. Диагональные элементы соседними не считаются.
    Элементы матрицы — целые числа, по модулю не превосходящие 1000.
    """
    numbers = []
    if coord_n > 0:
        numbers.append(table[coord_n-1][coord_m])
    if coord_m > 0:
        numbers.append(table[coord_n][coord_m-1])
    if coord_n < n - 1:
        numbers.append(table[coord_n+1][coord_m])
    if coord_m < m - 1:
        numbers.append(table[coord_n][coord_m+1])
    return ' '.join([str(x) for x in sorted(numbers)])


if __name__ == '__main__':
    n = int(input())  # строки
    m = int(input())  # столбцы
    table = [0] * n
    for i in range(n):
        table[i] = list(map(int, input().split()))
    coord_n = int(input())  # строки c 0
    coord_m = int(input())  # столбцы c 0
    numbers = neighbor(table, coord_n, coord_m)
    print(numbers)
