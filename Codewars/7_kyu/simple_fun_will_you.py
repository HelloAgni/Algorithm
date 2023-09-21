"""
Knowing whether a person is young, beautiful and loved,
find out if they contradict Mary's belief.

A person contradicts Mary's belief if one of the following statements is true:

>they are young and beautiful but not loved;
>they are loved but not young or not beautiful.

true if the person contradicts Mary's belief, false otherwise.
"""


def will_you(young, beautiful, loved):
    if len(set([young, beautiful, loved])) == 1:
        return False
    if loved is True:
        return True
    return young == beautiful


assert will_you(True, True, True) is False
assert will_you(False, False, False) is False
assert will_you(True, False, False) is False
assert will_you(False, True, False) is False
assert will_you(True, False, True) is True
assert will_you(False, False, True) is True
assert will_you(True, True, False) is True


def will_you_v2(young, beautiful, loved):
    return (young and beautiful) != loved


assert will_you_v2(False, True, False) is False
assert will_you_v2(True, False, True) is True
