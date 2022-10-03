import re


def check(s):
    """
    Write function which increments a string, to create a new string.
    If the string already ends with a number,
    the number should be incremented by 1.
    If the string does not end with a number.
    the number 1 should be appended to the new string.
    foo -> foo1
    foo0042 -> foo0043
    """
    new = re.sub(r'\d+$', '', s)
    numb = s.replace(new, '')
    print(f'Numbers at the end of the string: {numb}')
    if len(s) == len(new) or s == '':
        return s + '1'
    return new + str(int(numb)+1).zfill(len(numb))


item = 'foo0042'
item_2 = 'oEhb9449213S+$bd3H098082790808195685'
item_3 = ''
print(check(item))
print(check(item_2))
print(check(item_3))
