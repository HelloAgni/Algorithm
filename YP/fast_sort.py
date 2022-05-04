import random


def partition(array, pivot):
    left = [i for i in array if i < pivot]
    center = [i for i in array if i == pivot]
    right = [i for i in array if i > pivot]
    return left, center, right


def quicksort(array):
    if len(array) < 2:  # базовый случай,
        return array  # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = random.choice(array)
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


if __name__ == '__main__':
    array = [int(x) for x in input().split()]
    result = quicksort(array)
    print(result)
