from collections import Counter


def find_uniq(arr):
    """
    There is an array with some numbers.
    All numbers are equal except for one. Try to find it!
    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    """
    for k, v in Counter(arr).items():
        if v == 1:
            return k
    return k


arr = [1, 1, 1, 2, 1, 1]
print(find_uniq(arr))
