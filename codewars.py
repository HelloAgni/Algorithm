def add(n):
    """
    Create a function add(n)/Add(n) which returns
    a function that always adds n to any number
    Example:
    add_one = add(1)
    add_one(3)  # 4

    add_three = add(3)
    add_three(3) # 6
    """
    def add_s(x):
        print(n + x)
        return n + x
    return add_s

# v2


def add_v2(n):
    return lambda x: x + n


add_one = add(1)
add_one(3)
add_three = add(3)
add_three(3)
