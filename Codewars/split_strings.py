import re


def solution(s):
    """
     Splits the string into pairs of two characters.
     If the string contains an odd number of characters then
     it should replace the missing second character
     of the final pair with an underscore ('_').
    Examples:
    'abc' =>  ['ab', 'c_']
    'abcdef' => ['ab', 'cd', 'ef']
    """
    return re.findall(".{2}", s + "_")


def solution_v2(s):
    if len(s) % 2 != 0:
        s += '_'
    n = 2
    return [s[i:i+n] for i in range(0, len(s), n)]


st = 'abc'  # ['ab', 'c_']
b = 'abcdef'  # ['ab', 'cd', 'ef']
print(solution(st))
print(solution_v2(st))
