"""
Write a function that will check whether ANY permutation of the characters
of the input string is a palindrome.
Bonus points for a solution that is efficient and/or
that uses only built-in language functions.
Deem yourself brilliant if you can come up with a version
that does not use any function whatsoever.
Example:
madam -> True
adamm -> True
junk -> False
"""

from collections import Counter


def permute_a_palindrome(input):
    if input == '':
        return True
    elif len(input) % 2 == 0:
        return len(set([input.count(x) % 2 for x in input])) == 1
    return [x % 2 for x in list(Counter(input).values())].count(1) == 1


s_1 = 'madam'
s_2 = 'accca'
s_3 = 'aaa'
s_4 = ''
s_5 = 'xnhjrsxnmxrupflkgdggnwf'
print(permute_a_palindrome(s_1))
print(permute_a_palindrome(s_2))
print(permute_a_palindrome(s_3))
print(permute_a_palindrome(s_4))
print(permute_a_palindrome(s_5))
