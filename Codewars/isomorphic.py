def isomorph(a, b):
    """
    Create a function that return True
    if two given strings are isomorphic to each other,
    and False otherwise. Remember that order is important.
    True: CBAABC DEFFED
    False: AB CC
    """
    return [a.index(_) for _ in a] == [b.index(_) for _ in b]


def isomorph_v2(a, b):
    if len(a) != len(b):
        return False
    new_a, new_b = {}, {}
    for c, item in enumerate(a):
        if item in new_a:
            continue
        else:
            new_a[item] = c
    for c, item in enumerate(b):
        if item in new_b:
            continue
        else:
            new_b[item] = c
    return [new_a[x] for x in a] == [new_b[x] for x in b]


string_1 = 'ABCBACCAB'
string_2 = 'ABCBACCAB'
print(isomorph(string_1, string_2))
print(isomorph_v2(string_1, string_2))
