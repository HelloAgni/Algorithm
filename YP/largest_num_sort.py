def checker(num1, num2):
    if int(num1+num2) > int(num2+num1):
        return True


def largest_num(array, key):
    """
    Вывести самое большое число, которое можно составить из данных чисел.
    """
    for i in range(1, len(array)):
        item = array[i]
        j = i
        while j > 0 and key(item, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item
    return ''.join(array)


if __name__ == '__main__':
    n = int(input())  # количество чисел
    array = input().split()
    result = largest_num(array, checker)
    print(result)
