"""
Rules for a smiling face:
    Each smiley face must contain a valid pair of eyes.
    Eyes can be marked as : or ;
    A smiley face can have a nose but it does not have to.
    Valid characters for a nose are - or ~
    Every smiling face must have a smiling mouth
    that should be marked with either ) or D

No additional characters are allowed except for those mentioned.
Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]
"""
import re


def count_smileys(arr):
    return len([x for x in arr if re.match(r'[:;]{1}[-~]{,1}[D)]{1}', x)])


def count_smileys_v2(arr):
    return len(list(re.findall(r"[:;][-~]?[)D]", " ".join(arr))))


arr_1 = [':)', ';(', ';}', ':-D']  # return 2
arr_2 = [';D', ':-(', ':-)', ';~)']  # return 3
arr_3 = [';]', ':[', ';*', ':$', ';-D']  # return 1
assert count_smileys(arr_1) == 2
assert count_smileys(arr_2) == 3
assert count_smileys(arr_3) == 1
assert count_smileys_v2(arr_1) == 2
assert count_smileys_v2(arr_2) == 3
assert count_smileys_v2(arr_3) == 1
