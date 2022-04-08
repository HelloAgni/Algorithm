def nearest(house_numbers, n):
    """
    Выведите расстояние до ближайшего нуля.
    Числа выводите в одну строку, разделяя их пробелами.
    """
    distance = [0] + [*house_numbers] + [int(10**9)]
    print(distance)
    for i in range(n-2, -1, -1):
        if distance[i] != 0:
            distance[i] = distance[i+1] + 1
            print(distance)
    for i in range(2, n):
        if distance[i] != 0:
            distance[i] = min(distance[i-1] + 1, distance[i])
            print(distance)
    return distance[1:-1]


if __name__ == '__main__':
    n = int(input()) + 2
    house_numbers = map(int, input().split())
    distance = nearest(house_numbers, n)
    print(*distance)
