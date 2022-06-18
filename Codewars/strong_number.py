import math


def strong_num(number):
    """
    Strong number is the number that the sum
    of the factorial of its digits is equal to number itself.
    For example: 145, since
    1! + 4! + 5! = 1 + 24 + 120 = 145
    So, 145 is a Strong number.
    """
    factorial_sum = sum([math.factorial(int(x)) for x in str(number)])
    if factorial_sum == number:
        return "STRONG!!!!"
    return "Not Strong !!"


n = 145
print(strong_num(n))
