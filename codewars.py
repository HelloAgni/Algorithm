def difference_of_squares(n):
    """
    Find the difference between the sum of the squares of the first n
    natural numbers (1 <= n <= 100) and the square of their sum.
    Example
    For example, when n = 10:
    The square of the sum of the numbers is:
    (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)**2 = 55**2 = 3025
    The sum of the squares of the numbers is:
    12 + 22 + 32 + 42 + 52 + 62 + 72 + 82 + 92 + 102 = 385
    Difference Of Squares -> 3025 - 385 = 2640
    """
    sum_of_sq = (sum(x for x in range(n + 1)))**2
    sq_of_sum = sum(x**2 for x in range(n + 1))
    print(sum_of_sq - sq_of_sum)


# v2

def difference_of_squares_v2(n):
    s = range(n + 1)
    print((sum(s) ** 2) - (sum(x**2 for x in s)))


n = 10
difference_of_squares(n)
difference_of_squares_v2(n)
