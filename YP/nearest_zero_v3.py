def nearest(house_numbers):
    """
    Выведите расстояние до ближайшего нуля.
    Числа выводите в одну строку, разделяя их пробелами.
    """
    n = len(house_numbers)
    new = [0] * n
    first_zero = house_numbers.index(0)
    last_zero = n - 1 - house_numbers[::-1].index(0)

    if house_numbers.count(0) == 1 and first_zero == 0:
        print('opa 1')
        for x in range(n):
            if house_numbers[x] != 0:
                new[x] = new[x-1] + 1

    if house_numbers.count(0) == 1 and house_numbers[-1] == 0:
        print('opa в конце')
        for x in range(n-1, -1, -1):
            if house_numbers[x] != 0:
                new[x] = new[x+1] + 1

    else:
        for x in range(first_zero, n):
            if house_numbers[x] != 0:
                new[x] = new[x-1] + 1

        for x in range(last_zero, first_zero, -1):
            if house_numbers[x] != 0:
                new[x] = min(new[x], new[x+1] + 1)

        for x in range(first_zero, -1, -1):
            if house_numbers[x] != 0:
                new[x] = new[x+1] + 1
    print(*new)


if __name__ == '__main__':
    n = int(input())
    house_numbers = list(map(int, input().split()))
    nearest(house_numbers)
