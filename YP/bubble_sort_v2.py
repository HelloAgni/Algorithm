def bubble_sort(line):
    """
    Сортировка пузырьком.
    После каждого прохода по массиву, на котором
    какие-то элементы меняются местами, выводите его промежуточное состояние.
    """
    zero_swap = False
    while True:
        swapped = False
        for i in range(len(line)-1):
            if line[i] > line[i+1]:
                line[i], line[i + 1] = line[i + 1], line[i]
                swapped = True
                zero_swap = True
        if swapped is True:
            print(*line)
        else:
            break
    if zero_swap is False:
        print(*line)


if __name__ == '__main__':
    n = int(input())  # Длина массива
    line = [int(x) for x in input().split()]
    result = bubble_sort(line)
