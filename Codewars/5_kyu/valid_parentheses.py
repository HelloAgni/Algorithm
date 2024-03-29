import re


def valid_parentheses(string):
    """
    Write a function that takes a string of parentheses,
    and determines if the order of the parentheses is valid.
    The function should return true if the string is valid,
    and false if it's invalid.
    "()"              =>  true
    ")(()))"          =>  false
    """
    string = re.sub(r'\w', '', string)
    while '()' in string:
        string = string.replace('()', '')
    return not string


br = 'hi(hi)'
print(valid_parentheses(br))
