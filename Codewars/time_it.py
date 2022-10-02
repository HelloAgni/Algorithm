import timeit

check_1 = """
def big_range():
    new = []
    for x in range(1000):
        new.append(x**10)
    return new

big_range()
"""
print(timeit.timeit(check_1, number=1))


check_2 = """
def rgb_v2(r, g, b):
    rd = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(rd(r), rd(g), rd(b))

r, g, b = (148, 0, 211)
rgb_v2(r, g, b)
"""
print(timeit.timeit(check_2, number=1000))
