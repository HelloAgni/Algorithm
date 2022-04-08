import sys
from collections import Counter


def maximum_points(table, buttons_count):
    """
    На клавише написана либо точка, либо цифра от 1 до 9.
    В момент времени t игрок должен одновременно нажать на все клавиши,
    на которых написана цифра t.
    Игроки могут нажать в один момент времени на k клавиш каждый.
    Выведите единственное число –— максимальное количество баллов.
    """
    points = 0
    elements_count = Counter(''.join(table))
    for x in elements_count.values():
        if x <= buttons_count:
            points += 1
    return points


if __name__ == '__main__':
    buttons_count = int(input()) * 2
    table = []
    for _ in range(4):
        line = sys.stdin.readline().rstrip()
        table.append(line.replace('.', ''))
    points = maximum_points(table, buttons_count)
    print(points)
