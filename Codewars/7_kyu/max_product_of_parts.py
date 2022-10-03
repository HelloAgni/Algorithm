from functools import reduce
from operator import mul


def maximum_product_of_parts(n):
    """
    Given a written number, find the highest possible product from splitting
    it into three parts and multiplying those parts together. For example:
    product of [1 | 2 | 34] = 1 * 2 * 34 = 68
    product of [1 | 23 | 4] = 1 * 23 * 4 = 92
    product of [12 | 3 | 4] = 12 * 3 * 4 = 144
    So maximumProductOfParts(1234) = 144

    n = 1234 => 144
    n = 4321 => 252
    n = 4224 => 352
    """
    s = str(n)
    return max(reduce(mul, map(int, (s[:i], s[i:j], s[j:])))
               for i in range(1, len(s)-1) for j in range(i+1, len(s)))


n = 1234
print(maximum_product_of_parts(n))
