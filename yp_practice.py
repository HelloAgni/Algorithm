import sys

# 1
A, B = map(int, input().split())
print(A + B)

# 2
w = open('output.txt', 'w')

for x in open('input.txt', 'r'):
    d = sum(list(map(int, x.split())))
    print(d)
    w.write(str(d))


# 3
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()


def search():
    """
    Даны две строки строчных латинских символов: строка J и строка S.
    Символы, входящие в строку J, — «драгоценности»,
    входящие в строку S — «камни». Нужно определить, какое количество символов
    из S одновременно являются «драгоценностями».
    Проще говоря, нужно проверить, какое количество символов из S входит в J.
    """
    result = 0
    for ch in s:
        if ch in j:
            result += 1
    print(result)


search()
