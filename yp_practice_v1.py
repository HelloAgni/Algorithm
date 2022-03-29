def twosum_with_sort(numbers, X):
    # Сортируем исходный массив стандартной функцией.
    numbers.sort()

    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            print(numbers[left], numbers[right])
            return numbers[left], numbers[right]
        if current_sum < X:
            left += 1
        else:
            right -= 1
# Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
    return print(None)


n = int(input())
numbers = list(map(int, (input().split())))
k = int(input())
twosum_with_sort(numbers, k)
