from collections import Counter


def duplicate_count(text):
    """
    Write a function that will return the count of distinct case-insensitive
    alphabetic characters and numeric digits
    that occur more than once in the input string.
    Example
    "abcde" -> 0 # no characters repeats more than once
    "aabbcde" -> 2 # 'a' and 'b'
    "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
    """
    return len([x for x in Counter(text.lower()).values() if x > 1])


def duplicate_count_v2(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


text = 'Indivisibilities'  # 2
print(duplicate_count(text))
print(duplicate_count_v2(text))
