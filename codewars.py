def descending_order(num):
    """
    Make a function that can take any non-negative integer
    as an argument and return it with its digits in descending order.
    Input: 42145 Output: 54421
    Input: 145263 Output: 654321
    Input: 123456789 Output: 987654321
    """
    string = str(num)
    sorting = sorted(string, reverse=True)
    descend = ''.join(sorting)
    print(int(descend))


# v2

def descending_order_v2(num):
    print(int("".join(sorted(str(num), reverse=True))))


num = '145263'
descending_order(num)
descending_order_v2(num)
