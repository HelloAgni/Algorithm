# ex_1
def twosum(numbers, k):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == k:
                print(numbers[i], numbers[j])
                return
                # return numbers[i], numbers[j]
    # По условию задачи пара обязательно должна найтись.
    # если пара не найдена - вернём None, None (или можно выкинуть exception).
    return print(None)


n = int(input())
numbers = list(map(int, (input().split())))
k = int(input())
twosum(numbers, k)
