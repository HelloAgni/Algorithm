def fibo_num(n, k):
    """
    Выведите единственное число – последние k цифр числа Fn
    Если в искомом числе меньше k цифр,
    то выведите само число без ведущих нулей
    """
    x = 10 ** k
    new = [1] * 2
    for _ in range(n-1):
        new_sum = (new[0] + new[1]) % x
        new[0] = new[1]
        new[1] = new_sum
    return new[-1]


if __name__ == '__main__':
    n, k = map(int, input().split())
    fibo = fibo_num(n, k)
    print(fibo)
