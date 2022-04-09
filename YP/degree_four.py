import math


def degree_four(n):
    """
    Выведите «True», если число является степенью четырёх,
    «False» –— в обратном случае.
    """
    z = math.log(n, 4)
    if int(z) == z:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    n = int(input())
    degree_four(n)
