"""
The set of words is given. Words are joined if the last letter of one word
and the first letter of another word are the same.
Return true if all words of the set can be combined into one word.
Each word can and must be used only once. Otherwise return false
"""
from itertools import pairwise, permutations


def solution(arr):
    for perm in permutations(arr, len(arr)):
        if all(x[-1] == y[0] for x, y in pairwise(perm)):
            # print(perm)
            # ('desire', 'excavate', 'endure',
            # 'excess', 'screen', 'night', 'theater')

            # print(list(pairwise(perm)))
            # [('desire', 'excavate'), ('excavate', 'endure'),
            # ('endure', 'excess'), ('excess', 'screen'),
            # ('screen', 'night'), ('night', 'theater')]
            return True
    return False


arr_1 = [
    "excavate", "endure", "screen", "desire", "theater", "excess", "night"
    ]  # True
arr_2 = [
    "trade", "pole", "view", "grave", "ladder", "mushroom", "president"
    ]  # False
print(solution(arr_1))
print(solution(arr_2))
