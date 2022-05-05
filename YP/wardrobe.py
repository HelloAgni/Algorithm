def counting_sort(array):
    """
    В первой строке задано количество предметов в гардеробе: n <= 1000000
    Во второй строке даётся массив, в котором указан цвет для каждого предмета.
    Розовый цвет обозначен 0, жёлтый — 1, малиновый – 2.
    Вывести в строку через пробел цвета предметов в правильном порядке.
    """
    counted_values = [0] * 3
    for value in array:
        counted_values[value] += 1
    return ((str(0) + ' ')*counted_values[0],
            (str(1) + ' ')*counted_values[1],
            (str(2) + ' ')*counted_values[2])


if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in input().split()]
    result = counting_sort(array)
    print(*result, sep='')
