def ef_quick_sort(array, start, end):
    """
    В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
    В каждой из следующих n строк задана информация про одного из участников.
    i-й участник описывается тремя параметрами:
    > уникальным логином (строкой из маленьких латинских букв длиной <= 20)
    > числом решённых задач Pi
    > штрафом Fi
    Для отсортированного списка участников
    выведите по порядку их логины по одному в строке.
    """
    if start >= end:
        return array
    pivot = array[start]
    left = start
    right = end
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    ef_quick_sort(array, start, right)
    ef_quick_sort(array, left, end)
    return array


if __name__ == '__main__':
    n = int(input())
    participants = []
    for _ in range(n):
        login, tasks, penalty = input().split()
        participants.append([-int(tasks), int(penalty), login])
    start, end = 0, n-1
    result = ef_quick_sort(participants, start, end)
    for _ in result:
        print(_[-1])
