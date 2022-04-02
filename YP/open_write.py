def change_txt(file):
    for x in file:
        d = sum(list(map(int, x.split())))
        print(d)
        w.write(str(d))


if __name__ == '__main__':
    w = open('output.txt', 'w')
    file = open('input.txt', 'r')
    change_txt(file)
