def is_triangle(a, b, c):
    """
    Implement a function that accepts 3 integer values a, b, c.
    The function should return true if a triangle can be built
    with the sides of given length and false in any other case.
    (In this case, all triangles must have surface greater than 0).
    """
    if (a + b) > c and (b + c) > a and (a + c) > b:
        print(True)
    else:
        print(False)

# v2


def is_triangle_v2(a, b, c):
    print((a < b + c) and (b < a + c) and (c < a + b))


a = 7
b = 2
c = 2
is_triangle(a, b, c)
is_triangle_v2(a, b, c)

