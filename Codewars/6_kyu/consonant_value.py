"""
Given a lowercase string that has alphabetic characters only and no spaces,
return the highest value of consonant substrings.

-- The consonant substrings are: "z", "d" and "cs"
and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
solve("zodiacs") = 26
"""
import re


def solve(s):
    new = re.split(r'[aeiou]', s)

    def sum_of_letters(letters):
        return sum([ord(x) % 32 for x in letters])

    return max([sum_of_letters(x) for x in new])


print(solve("zodiacs"))
