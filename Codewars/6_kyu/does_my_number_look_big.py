def narcissistic(value):
    """
    A Narcissistic Number (or Armstrong Number) is a positive number
    which is the sum of its own digits, each raised to
    the power of the number of digits in a given base.
    Return True or False depending upon whether the given number
    is a Narcissistic number in base 10
    For example, take 153 (3 digits), which is narcisstic:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    """
    degree = len(str(value))
    return sum([int(x)**degree for x in str(value)]) == value


print(narcissistic(153))
