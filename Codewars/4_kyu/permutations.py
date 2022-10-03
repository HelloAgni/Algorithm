from itertools import permutations as p
import timeit


def permutations(s):
    """
    create all permutations of a non-empty
    input string and remove duplicates
    * With input 'aabb'
    * Your function should return [
        'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    """
    return [''.join(x) for x in set(p(s))]


def permutations_v2(s):
    return (''.join(x) for x in set(p(s)))


st = 'abba'
print(permutations(st), permutations_v2(st))

check_comprehension = """
from itertools import permutations as p
def permutations(s):
    return [''.join(x) for x in set(p(s))]

s = 'abbbaa'
permutations(s)
"""

check_generator = """
from itertools import permutations as p
def permutations_v2(s):
    return list(''.join(x) for x in set(p(s)))

s = 'abbbaa'
permutations_v2(s)
"""
print(
    timeit.timeit(check_comprehension, number=1000),
    timeit.timeit(check_generator, number=1000))
