def capitalize(s,  ind):
    """
    Given a string and an array of integers representing indices,
    capitalize all letters at the given indices.
    For example:
    capitalize("abcdef",[1,2,5]) = "aBCdeF"
    capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
    """
    s = list(s)
    for count, x in enumerate(s):
        if count in ind:
            s[count] = s[count].upper()
    print(s)
    print(''.join(s))

# v2


def capitalize_v2(s, ind):
    ind = set(ind)
    print(''.join(c.upper() if i in ind else c for i, c in enumerate(s)))


s = 'abcdef'  # "aBCdeF"
ind = [1, 2, 5, 100]
capitalize(s, ind)
capitalize_v2(s, ind)
