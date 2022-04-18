def nearest(house_numbers, n):
    """
    Выведите расстояние до ближайшего нуля.
    Числа выводите в одну строку, разделяя их пробелами.
    """
    count = n
    for i in range(n):
        if house_numbers[i] == 0:
            count = 0
        else:
            count += 1
            house_numbers[i] = count
    for i in range(n - 1, -1, -1):
        if house_numbers[i] == 0:
            count = 0
        else:
            count += 1
            house_numbers[i] = min(count, house_numbers[i])
    return house_numbers


if __name__ == '__main__':
    n = int(input())
    house_numbers = list(map(int, input().split()))
    new = nearest(house_numbers, n)
    print(*new)
