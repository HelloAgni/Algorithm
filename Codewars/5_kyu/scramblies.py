import timeit

from collections import Counter


def scramble(s1, s2):
    """
    Complete the function that returns true
    if a portion of str1 characters can be rearranged to match str2,
    otherwise returns false
    scramble('cedewaraaossoqqyt', 'codewars') ==> True
    scramble('katas', 'steak') ==> False
    """
    if Counter(s2) - Counter(s1):
        return False
    return True


def scramble_v2(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


a_0 = 'rkqodlw'  # True
b_0 = 'world'
a_1 = 'cedewaraaossoqqyt'  # True
b_1 = 'codewars'
a_2 = 'katas'  # False
b_2 = 'steak'
print(scramble(a_0, b_0), scramble_v2(a_0, b_0))
print(scramble(a_1, b_1), scramble_v2(a_1, b_1))
print(scramble(a_2, b_2), scramble_v2(a_2, b_2))

check_counter = """
from collections import Counter
def scramble(s1, s2):
    if Counter(s2) - Counter(s1):
        return False
    return True
s1 = 'katas'
s2 = 'steak'
scramble(s1, s2)
"""
check_count = """
def scramble_v2(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True
s1 = 'katas'
s2 = 'steak'
scramble_v2(s1, s2)
"""
print('check_count faster than Counter ->', timeit.timeit(
        check_counter, number=100000) > timeit.timeit(
        check_count, number=100000))
print(timeit.timeit(check_count, number=100000), timeit.timeit(
        check_counter, number=100000))
