import re


def solve(s):
    """
    The vowel substrings in the word codewarriors are o,e,a,io.
    The longest of these has a length of 2.
    Given a lowercase string that has alphabetic characters only
    (both vowels and consonants) and no spaces,
    return the length of the longest vowel substring. Vowels are any of aeiou.
    """
    y = re.split(r'(?=[^oeaiou])', s)
    print(y)
    long = max(y, key=len)
    print(len(long)-1)


# v2
def solve_v2(s):
    print(
        max(map(len, ''.join(c if c in 'aeiou' else ' ' for c in s).split()))
        )


s = 'chrononhotonthuooaos'  # 5
solve(s)
solve_v2(s)
