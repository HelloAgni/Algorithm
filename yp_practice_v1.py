def twosum_extra_ds(numbers, k):
    # Создаём вспомогательную структуру данных с быстрым поиском элемента.
    previous = set()

    for a in numbers:
        y = k - a
        if y in previous:
            print(y, a)
            return a, y
        else:
            previous.add(a)
    # Если ничего не нашлось в цикле, значит,пары элементов в массиве нет.
    return print(None)


n = int(input())
numbers = list(map(int, (input().split())))
k = int(input())
twosum_extra_ds(numbers, k)
