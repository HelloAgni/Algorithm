def fibo_num(n):
    """
    Для всех i≥2 выполнено Fi=F(i-1) + F(i-2)
    найдите Fn
    Решение должно быть реализовано рекурсивно.
    На вход подаётся n — целое число в диапазоне от 0 до 32
    """
    if n == 1 or n == 0:
        return 1
    return fibo_num(n-1) + fibo_num(n-2)


if __name__ == '__main__':
    n = int(input())
    fibo = fibo_num(n)
    print(fibo)
