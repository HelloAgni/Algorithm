"""
In this kata, your task is to create a regular expression capable
of evaluating binary strings (strings with only 1s and 0s)
and determining whether the given string represents a number divisible by 3.

Take into account that:
    > An empty string might be evaluated to true
    (it's not going to be tested, so you don't need
    to worry about it - unless you want)
    > The input should consist only of binary digits - no spaces,
    other digits, alphanumeric characters, etc.
    > There might be leading 0s.
"""

import re

PATTERN = re.compile(r'^(1(01*0)*1|0)+$')


def check(arr: list[str]):
    return [True if re.match(PATTERN, x) else False for x in arr]


arr = ['000', '001', '011', '110', 'abc', ' 0']
result = [True, False, True, True, False, False]
assert check(arr=arr) == result, 'Somthing going wrong!'
