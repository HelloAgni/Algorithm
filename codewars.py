import math
import simple_decorator


@simple_decorator.timer
def strong_num(number):
    """
    Strong number is the number that the sum of the factorial
    of its digits is equal to number itself.
    For example: 145, since
    1! + 4! + 5! = 1 + 24 + 120 = 145
    So, 145 is a Strong number.
    """
    s = 0
    lst = list(str(number))
    for x in lst:
        s += math.factorial(int(x))
    if number == s:
        print('strong!')
    else:
        print('is not strong!')

# v2


number = 145
strong_num(number)
