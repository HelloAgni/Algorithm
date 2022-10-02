import timeit

check_1 = """
def big_range():
    new = []
    for x in range(1000):
        new.append(x**10)
    return new

big_range()
"""
print(timeit.timeit(check_1, number=1))

check_2 = """
def rgb_v2(r, g, b):
    rd = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(rd(r), rd(g), rd(b))

r, g, b = (148, 0, 211)
rgb_v2(r, g, b)
"""
print(timeit.timeit(check_2, number=1000))

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
print(timeit.timeit(check_count, number=100000), timeit.timeit(
        check_counter, number=100000))
