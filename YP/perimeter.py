def perimeter(array, n):
    """
    Из трёх отрезков с длинами a ≤ b ≤ c можно составить треугольник,
    если выполнено неравенство треугольника: c < a + b.
    Нужно вывести одно число — наибольший периметр треугольника.
    """
    # array.sort(key=lambda x: x*(-1))
    array.sort(reverse=True)
    find_perimeter = 0
    for c in range(n-2):
        if array[c] < (array[c + 1] + array[c + 2]):
            find_perimeter += 1
        if find_perimeter == 1:
            return array[c] + array[c + 1] + array[c + 2]


if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in input().split()]
    result = perimeter(array, n)
    print(result)
