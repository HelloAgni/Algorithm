def two_bikes(days, s_one, left, right):
    """
    По заданной стоимости велосипеда определить:
    - первый день, в которой возможно купить один велосипед,
    - первый день, в который возможно купить два велосипеда.
    Подсказка: решение должно работать за O(log n).
    """
    if right <= left:
        return -1
    mid = (left + right) // 2
    if days[mid - 1] < s_one <= days[mid] or mid == 0:
        return mid + 1
    elif s_one <= days[mid]:  # искомый элемент меньше центрального
        return two_bikes(days, s_one, left, mid)
    else:  # иначе следует искать в правой половине
        return two_bikes(days, s_one, mid + 1, right)


if __name__ == '__main__':
    n = int(input())  # число дней
    days = [int(x) for x in input().split()]  # количество накоплений за день
    s_one = int(input())  # стоимость
    result = two_bikes(days, s_one, left=0, right=len(days))
    result_2 = two_bikes(days, s_one*2, left=0, right=len(days))
    print(result, result_2)
