def order_weight(strng):
    """
    The weight of a number will be from now on the sum of its digits.
    For example 99 will have "weight" 18, 100 will have "weight" 1
    so in the list 100 will come before 99.
    "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:
    "100 180 90 56 65 74 68 86 99"
    """
    a = [x for x in strng.split()]
    b = [sum([int(x) for x in '!'.join(x).split('!')]) for x in strng.split()]
    c = tuple(zip(a, b))
    d = sorted(c, key=lambda x: (x[1], x[0]))
    result = ' '.join([x[0] for x in d])
    return result


def order_weight_v2(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))


arr = "56 65 74 100 99 68 86 180 90"
print(order_weight(arr))
print(order_weight_v2(arr))
