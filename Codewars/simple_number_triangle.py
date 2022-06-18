from math import factorial


def solve(n):
    """
    Consider the number triangle below, in which each number is equal
    to the number above plus the number to the left.
    If there is no number above, assume it's a 0.
    1
    1 1
    1 2 2
    1 3 5 5
    1 4 9 14 14
    The triangle has 5 rows and the sum of the last row is
    sum([1,4,9,14,14]) = 42.
    """
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))


n = 5
print(solve(n))
