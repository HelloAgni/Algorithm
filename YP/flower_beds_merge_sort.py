def flower_beds(new, n):
    """
    Нужно вывести координаты каждой из получившихся клумб
    в отдельных строках. Данные должны выводится в
    отсортированном порядке — сначала клумбы с меньшими координатами,
    затем — с бОльшими.
    """
    new2 = []
    new.sort()
    s = new[0][0]
    e = new[0][-1]
    for x in range(n-1):
        if e < new[x+1][0]:
            new2.append([s, e])
            s = new[x+1][0]
            e = new[x+1][-1]
        if e < new[x+1][-1]:
            e = new[x+1][-1]
    new2.append([s, e])
    return new2


if __name__ == '__main__':
    n = int(input())
    new = []
    for _ in range(n):
        line = [int(x) for x in input().split()]
        new.append(line)
    result = flower_beds(new, n)
    for _ in result:
        print(*_)
