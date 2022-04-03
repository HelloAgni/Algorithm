def factorial(n):
    """
    В единственной строке дано число n (2 ≤ n ≤ 109),
    которое нужно факторизовать.
    Выведите в порядке неубывания простые множители,
    на которые раскладывается число n.
    """
    prime = []
    x = 2
    while x * x <= n:
        if n % x == 0:
            prime.append(x)
            n //= x
        else:
            x += 1
    if n > 1:
        prime.append(n)
    print(*prime)


if __name__ == '__main__':
    n = int(input())
    factorial(n)
