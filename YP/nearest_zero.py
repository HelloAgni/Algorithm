def nearest(house_numbers):
    """
    Выведите расстояние до ближайшего нуля.
    Числа выводите в одну строку, разделяя их пробелами.
    """
    x = [0] + [*house_numbers] + [int(10**9)]
    n = len(x)
    for i in range(n-2, -1, -1):
        if x[i] != 0:
            x[i] = x[i+1] + 1
    for i in range(2, n):
        if x[i] != 0:
            x[i] = min(x[i-1] + 1, x[i])
    print(*x[1:-1])


if __name__ == '__main__':
    n = int(input())
    house_numbers = map(int, input().split())
    nearest(house_numbers)
