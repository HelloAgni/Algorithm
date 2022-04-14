import sys


def new_matrix(matrix):
    """
    Напечатайте транспонированную матрицу в том же формате,
    который задан во входных данных.
    Каждая строка матрицы выводится на отдельной строке,
    элементы разделяются пробелами.
    """
    new = list(zip(*matrix))
    return [' '.join(x) for x in new]


if __name__ == '__main__':
    n = int(input())  # строки
    m = int(input())  # столбцы
    matrix = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        matrix.append([x for x in line.split()])
    new = new_matrix(matrix)
    print(*new, sep='\n')
