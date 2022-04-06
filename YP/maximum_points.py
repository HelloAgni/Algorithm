import sys
from collections import Counter


def maximum_points():
    """
    На клавише написана либо точка, либо цифра от 1 до 9.
    В момент времени t игрок должен одновременно нажать на все клавиши,
    на которых написана цифра t.
    Игроки могут нажать в один момент времени на k клавиш каждый.
    Выведите единственное число –— максимальное количество баллов.
    """
    k = int(input()) * 2
    points = 0
    table = []
    for i in range(4):
        line = sys.stdin.readline().rstrip()
        table.append(line.replace('.', ''))
    t = Counter(''.join(table))
    for x in t.values():
        if x <= k:
            points += 1
    print(points)


if __name__ == '__main__':
    maximum_points()
