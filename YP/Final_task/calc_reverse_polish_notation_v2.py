def calc(line, operations):
    """
    В единственной строке дано выражение,
    записанное в обратной польской нотации.
    Числа и арифметические операции записаны через пробел.
    На вход могут подаваться операции: +, -, *, / и числа,
    по модулю не превосходящие 10000.
    Выведите единственное число — значение выражения.
    """
    new = []
    count = 0
    for i in line:
        if i == '+':
            new[count - 2] = new[count - 2] + new[count - 1]
            count -= 1
            new.pop()
        if i == '-':
            new[count - 2] = new[count - 2] - new[count - 1]
            count -= 1
            new.pop()
        if i == '*':
            new[count - 2] = new[count - 2] * new[count - 1]
            count -= 1
            new.pop()
        if i == '/':
            new[count - 2] = new[count - 2] // new[count - 1]
            count -= 1
            new.pop()
        if i not in operations:
            new.append(i)
            count += 1
    return new[-1]


if __name__ == '__main__':
    operations = ['+', '-', '*', '/']
    line = input().split()
    line = [int(x) if x not in operations else x for x in line]
    result = calc(line, operations)
    print(result)
