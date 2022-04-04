from collections import Counter


def extra(s, t):
    """
    На вход подаются строки s и t, разделённые переносом строки.
    Выведите лишнюю букву.
    """
    x = Counter(s)
    y = Counter(t)
    for i in y:
        if y[i] != x[i]:
            print(i)


if __name__ == '__main__':
    s = input()
    t = input()  # на 1 букву больше
    extra(s, t)
