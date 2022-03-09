import re


def min_value(digits):
    """
    Given a list of digits, return the smallest number,
    that could be formed from these digits,
    using the digits only once (ignore duplicates).
    Example:
    minValue({1, 9, 3, 1, 7, 4, 6, 6, 7}) return  ==> (134679)
    """
    x = sorted(set(digits))
    print(x)
    print(type(x))
    y = int(re.sub(r'\W', '', str(sorted(set(digits)))))
    print(y)

# v2


def min_value_v2(digits_v2):
    print(int(''.join(map(str, sorted(set(digits_v2))))))


digits_v2 = [1, 9, 3, 1, 7, 4, 6, 6, 7]
digits = [8, 1, 4, 4]
min_value(digits)
min_value_v2(digits_v2)
