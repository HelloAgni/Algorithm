def bubble_sort(array, n):
    """
    Сортировка пузырьком.
    После каждого прохода по массиву, на котором
    какие-то элементы меняются местами, выводите его промежуточное состояние.
    """
    change = 1
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                change = 1
        if change == 1:
            print(*array)
            change = 0


if __name__ == '__main__':
    n = int(input())  # Длина массива
    array = [int(x) for x in input().split()]
    bubble_sort(array, n)
