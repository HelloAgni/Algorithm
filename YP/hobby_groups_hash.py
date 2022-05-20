def hobby_groups(hash):
    """
    Выведите уникальные названия кружков по одному на строке,
    в порядке появления во входных данных.
    """
    return list(hash.keys())


if __name__ == '__main__':
    n = int(input())
    hash = {}
    for x in range(n):
        line = input()
        if line not in hash:
            hash[line] = True
    result = hobby_groups(hash)
    print(*result, sep='\n')
