"""
You will be given a list with the coefficients of a polynomial.
Look the following order in both:

P(x) =       6x³ + 3x² + 5x -4
coefficients =  [ 6,   3,    5, -4]

Your task is to express the polynomial
like a string with its value for a certain determinate x:

[6, 3, 5, -4], 4 returns
"For 6*x^3 + 3*x^2 + 5*x - 4 with x = 4 the value is 448"
"""

import re


def calc_poly(pol_list, x):
    degree = [x**y for y in range(len(pol_list) - 1, -1, -1)]
    result = sum([(x * degree[c]) for c, x in enumerate(pol_list)])

    expr = " + ".join(f"{c}*x^{-i}" for i, c in enumerate(
        pol_list, 1 - len(pol_list)) if c)
    expr = re.sub(r"(\^1\b|\b1\*)", "", expr.replace(
        "+ -", "- ").replace("*x^0", ""))
    return f"For {expr} with x = {x} the value is {result}"


assert calc_poly([6, 3, 5, -4], 4) == (
    "For 6*x^3 + 3*x^2 + 5*x - 4 with x = 4 the value is 448")
assert calc_poly([2, 0, 5, -6, 4, 0], 2) == (
    "For 2*x^5 + 5*x^3 - 6*x^2 + 4*x with x = 2 the value is 88")
print(calc_poly([6, 3, 5, -4], 4))
