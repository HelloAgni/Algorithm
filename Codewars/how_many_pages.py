def amount_of_pages(summary):
    """
    Given the summary, find the number of pages n the book has.
    Example
    If the input is summary=25, then the output must be n=17:
    The numbers 1 to 17 have 25 digits in total: 1234567891011121314151617
    """
    # 1-9:          9       = 9 * 1 * 10**0
    # 10-99:        180     = 9 * 2 * 10**1
    # 100-999:      2700    = 9 * 3 * 10**2
    # 1000-9999:    36000   = 9 * 4 * 10**3
    # 10000-99999:  450000  = 9 * 5 * 10**4
    res = 0
    for x in range(1, 6):
        y = 9 * x * 10**(x-1)
        if summary <= y:
            return res + summary//x
        res += y//x
        summary -= y


def amount_of_pages_v2(summary):
    if summary < 10:
        return summary
    if 10 <= summary <= 187:  # 99 => 89 * 2 + 10
        return int((summary + 9) / 2)
    if 188 <= summary <= 2884:  # 999 => 899 * 3 + 187
        return int((summary + 9 + 99) / 3)
    if 2885 <= summary <= 38800:  # 9999 => 8999 * 4 + 2884
        return int((summary + 9 + 99 + 999) / 4)
    if 38801 <= summary <= 488795:  # 99999 => 89999 * 5 + 38800
        return int((summary + 9 + 99 + 999 + 9999) / 5)
    if summary > 488796:  # > 100.000
        return int((summary + 9 + 99 + 999 + 9999 + 99999) / 6)


s = 185  # 97
print(amount_of_pages(s))
print(amount_of_pages_v2(s))
