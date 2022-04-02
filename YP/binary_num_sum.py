def binary_num_sum(n, m):
    """
    Два числа записаны в двоичной системе счисления.
    Нужно вывести их сумму, также в двоичной системе
    """
    num1 = n[::-1]  # перевернуть числа для удобства выполнения операций
    num2 = m[::-1]
    size = max(len(num1), len(num2))  # дополнить числа нулями
    num1 += [0] * (size - len(num1))
    num2 += [0] * (size - len(num2))
    overflow = 0
    res = []
    for obj in zip(num1, num2):  # сложить 2 числа
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        res.append(value % 2)
    if overflow == 1:
        res.append(1)  # перевернуть число назад
    res = res[::-1]
    print(''.join(map(str, res)))


if __name__ == '__main__':
    n = list(map(int, (input())))
    m = list(map(int, (input())))
    binary_num_sum(n, m)
