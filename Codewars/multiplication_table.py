import timeit


def multiplication_table(size):
    """
    Create NxN multiplication table,
    of size provided in parameter.
    for example, when given size is 3:
    1 2 3
    2 4 6
    3 6 9
    for given example, the return value should be:
    [[1,2,3],[2,4,6],[3,6,9]]
    """
    x = 0
    new = []
    while x != size:
        x += 1
        new.append([y+x for y in range(0, size*x, x)])
    return new


s = 3
print(multiplication_table(s))


check = """
def multiplication_table_t(size):
    x = 0
    new = []
    while x != size:
        x += 1
        new.append([y+x for y in range(0, size*x, x)])
    return new

size = 33
multiplication_table_t(size)
"""

print(round(timeit.timeit(check, number=1), 7))
