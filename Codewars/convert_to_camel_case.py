import re


def to_camel_case(text):
    """
    Converts dash/underscore delimited words into camel casing.
    The first word within the output should be capitalized only
    if the original word was capitalized
    Examples:
    "the-stealth-warrior" gets converted to "theStealthWarrior"
    "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
    """
    if text == '':
        return text
    else:
        r = text[0]
        new = list(re.sub(r'-|_', '', text.title()))
        new[0] = r
        return ''.join(new)


print(to_camel_case(text='The_Stealth_Warrior'))
print(to_camel_case(text='the-stealth-warrior'))
