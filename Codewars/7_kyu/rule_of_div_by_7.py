"""
Examples:
m = 371 -> 37 - (2*1) -> 37 - 2 = 35;
thus, since 35 is divisible by 7, 371 is divisible by 7.
The number of steps to get the result is 1.

m = 1603 -> 160 - (2 x 3) -> 154 -> 15 - 8 = 7 and 7 is divisible by 7.

m = 372 -> 37 - (2*2) -> 37 - 4 = 33;
thus, since 33 is not divisible by 7, 372 is not divisible by 7.

m = 477557101->47755708->4775554->477547->47740->4774->469->28
and 28 is divisible by 7, so is 477557101. The number of steps is 7.
"""


def seven(m):
    c = 0
    while m > 100:
        m = int(str(m)[:-1]) - int(str(m)[-1]) * 2
        c += 1
    return m, c


assert seven(1603) == (7, 2)
assert seven(371) == (35, 1)
assert seven(483) == (42, 1)
assert seven(483595) == (28, 4)


def seven_v2(m):
    c = 0
    while m > 100:
        m = m // 10 - 2 * (m % 10)
        c += 1
    return m, c


assert seven_v2(1603) == (7, 2)
assert seven_v2(371) == (35, 1)
assert seven_v2(483) == (42, 1)
assert seven_v2(483595) == (28, 4)
