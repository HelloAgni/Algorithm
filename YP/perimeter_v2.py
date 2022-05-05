import random


def partition(array, pivot):
    left = [i for i in array if i < pivot]
    center = [i for i in array if i == pivot]
    right = [i for i in array if i > pivot]
    return left, center, right


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        left, center, right = partition(array, pivot)
        # return quicksort(left) + center + quicksort(right)
        return quicksort(right) + center + quicksort(left)  # reverse


def perimeter(array, n):
    """
    Из трёх отрезков с длинами a ≤ b ≤ c можно составить треугольник,
    если выполнено неравенство треугольника: c < a + b.
    Нужно вывести одно число — наибольший периметр треугольника.
    """
    find_perimeter = 0
    for c in range(n-2):
        if array[c] < (array[c + 1] + array[c + 2]):
            find_perimeter += 1
        if find_perimeter == 1:
            return array[c] + array[c + 1] + array[c + 2]


if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in input().split()]
    sort_array_rev = quicksort(array)
    result = perimeter(sort_array_rev, n)
    print(result)
