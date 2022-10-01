import timeit

check_1 = """
def big_range():
    new = []
    for x in range(100000):
        new.append(x**10)
    return new
"""
print(timeit.timeit(check_1))


check_2 = """
r, g, b = (148, 0, 211)
def rgb_v2(r, g, b):
    rd = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(rd(r), rd(g), rd(b))
"""
print(timeit.timeit(check_2))
