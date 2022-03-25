from collections import Counter

from my_decorators import simple_decorator


@simple_decorator.timer
def find_uniq(arr):
    """
    There is an array with some numbers.
    All numbers are equal except for one. Try to find it!
    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    """
    for z, x in dict(Counter(arr)).items():
        if x == 1:
            print(z)

# v2


@simple_decorator.timer
def find_uniq_v2(arr):
    a, b = set(arr)
    print(a if arr.count(a) == 1 else b)


arr = [1, 1, 1, 2, 1, 1]  # 2
find_uniq(arr)
find_uniq_v2(arr)
