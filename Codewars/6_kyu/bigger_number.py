import timeit


def count_change(money, coins):
    """
    Create a function that takes a positive integer and returns
    the next bigger number that can be formed by rearranging its digits.
    For example:
    12 ==> 21
    513 ==> 531
    2017 ==> 2071
    """
    n = len(coins)

    def new(money, coins, n):
        if money == 0:
            return 1
        elif n == 0 or money < 0:
            return 0
        else:
            return new(
                money, coins, n - 1) + new(money - coins[n - 1], coins, n)
    return new(money, coins, n)


def count_change_v2(money, coins):
    if money < 0:
        return 0
    if money == 0:
        return 1
    if money > 0 and not coins:
        return 0
    return count_change_v2(money-coins[-1], coins) + count_change_v2(money, coins[:-1])


m = 10
arr = [5, 2, 3]
print(count_change(m, arr))
print(count_change_v2(m, arr))

check_1 = """
def count_change(money, coins):
    n = len(coins)

    def new(money, coins, n):
        if money == 0:
            return 1
        elif n == 0 or money < 0:
            return 0
        else:
            return new(
                money, coins, n - 1) + new(money - coins[n - 1], coins, n)
    return new(money, coins, n)
m = 10
arr = [5, 2, 3]
count_change(m, arr)
"""

check_2 = """
def count_change_v2(money, coins):
    if money < 0:
        return 0
    if money == 0:
        return 1
    if money > 0 and not coins:
        return 0
    return count_change_v2(money-coins[-1], coins) + count_change_v2(money, coins[:-1])
m = 10
arr = [5, 2, 3]
count_change_v2(m, arr)
"""

print(timeit.timeit(check_1, number=1000) < timeit.timeit(check_2, number=1000))
