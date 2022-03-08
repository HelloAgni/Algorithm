def accum(s):
    """
    Examples:
    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"
    """
    count = 0
    new_list = []
    for x in s:
        count += 1
        new_list.append(x*count)
    print(new_list)
    print('-'.join(new_list).title())


# v2

def accum_v2(s):
    print('-'.join(c.upper() + c.lower() * i for i, c in enumerate(s)))


s = "RqaEzty"
accum(s)
accum_v2(s)
