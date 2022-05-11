from collections import Counter


def find_children(dancing_brigade):
    """
    "aAbaBb" => "AaaBbb".
    """
    new = ''
    s = [x.lower() for x in dancing_brigade]
    d = Counter(sorted(s))
    for x in d:
        new += (x * d[x]).title()
    return new


def find_children_v2(dancing_brigade):
    return ''.join(sorted(
        dancing_brigade, key=lambda x: (x.upper(), x.islower())))


dancing_brigade = 'zzZzAaaBbbaa'
print(find_children(dancing_brigade))
print(find_children_v2(dancing_brigade))
