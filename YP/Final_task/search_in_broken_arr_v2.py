def binary_s(arr, x, left, right):
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    if right <= left:
        return -1
    if arr[left] <= arr[mid]:
        if arr[mid] > x >= arr[left]:
            return binary_s(arr, x, left, mid)
        else:
            return binary_s(arr, x, mid + 1, right)
    if arr[left] > arr[mid]:
        if arr[mid] < x <= arr[right]:
            return binary_s(arr, x, mid + 1, right)
        else:
            return binary_s(arr, x, left, mid)


def broken_search(nums, target):
    """
    Функция должна вернуть индекс элемента, равного k
    Eсли такой есть в массиве (нумерация с нуля).
    Если элемент не найден, функция должна вернуть -1
    Изменять массив нельзя.
    """
    return binary_s(nums, target, left=0, right=len(nums)-1)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
