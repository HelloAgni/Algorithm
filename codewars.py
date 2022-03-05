def xo(s):
    """
    XO("ooxx") => true
    XO("xooxx") => false
    XO("ooxXm") => true
    XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
    XO("zzoo") => false
    """

    s = s.lower()
    return s.count('x') == s.count('o')


print(xo.__doc__)
