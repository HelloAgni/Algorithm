def collatz(n):
    """
          n/2, if n is even
    f(n)={
          3n+1, if n is odd
    Input: 4
    Output: "4->2->1"
    Input: 3
    Output: "3->10->5->16->8->4->2->1"
    """
    new = [str(n)]
    while n:
        if n % 2 == 0:
            n = int(n/2)
            new.append(str(n))
        if n == 1:
            return '->'.join(new)
        if n % 2 != 0:
            n = int(3 * n + 1)
            new.append(str(n))


def collatz_v2(n):
    new = [str(n)]
    while n > 1:
        n = int(3 * n + 1 if n % 2 else n/2)
        new.append(str(n))
    return '->'.join(new)


num = 3
print(collatz(num))
print(collatz_v2(num))
