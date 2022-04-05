def extra_v2(s, t):
    """
    На вход подаются строки s и t, разделённые переносом строки.
    Выведите лишнюю букву.
    """
    for i in s:
        t = t.replace(i, '', 1)
    print(t)


if __name__ == '__main__':
    s = input()
    t = input()  # на 1 букву больше
    extra_v2(s, t)
