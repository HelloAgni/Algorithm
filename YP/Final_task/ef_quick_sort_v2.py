import random


def partition(array, pivot):
    left = [i for i in array if i < pivot]
    center = [i for i in array if i == pivot]
    right = [i for i in array if i > pivot]
    return left, center, right


def ef_quick_sort(array):
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
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        left, center, right = partition(array, pivot)
        return ef_quick_sort(left) + center + ef_quick_sort(right)


if __name__ == '__main__':
    n = int(input())
    participants = []
    for _ in range(n):
        login, tasks, penalty = input().split()
        participants.append([-int(tasks), int(penalty), login])
    result = ef_quick_sort(participants)
    for _ in result:
        print(_[-1])
