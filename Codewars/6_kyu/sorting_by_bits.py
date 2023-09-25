"""
In this kata you're expected to sort an array of 32-bit integers
in ascending order of the number of on bits they have.

Example:
[3, 8, 3, 6, 5, 7, 9, 1]   =>    [1, 8, 3, 3, 5, 6, 9, 7]
"""


def sortByBit(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr


b = [3, 8, 3, 6, 5, 7, 9, 1]
print(sortByBit(b))
