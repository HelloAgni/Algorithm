"""
A pangram is a sentence that contains every single letter
of the alphabet at least once. For example, the sentence
"The quick brown fox jumps over the lazy dog"
is a pangram, because it uses the letters A-Z at least once
(case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not.
Ignore numbers and punctuation.
"""
import re


def is_pangram(s):
    return len(set(re.sub(r'[^a-zA-Z]', '', s.lower()))) == 26


s_1 = 'The123 quick brown - asd fox .......jumps ,,,,,,,over the lazy dog'
s_2 = 'Abcd'

print(is_pangram(s_1))
print(is_pangram(s_2))
