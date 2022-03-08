
def is_isogram(string):
    """
    An isogram is a word that has no repeating letters,
    consecutive or non-consecutive.
    Assume the empty string is an isogram. Ignore letter case.
    Example: (Input --> Output)
    "Dermatoglyphics" --> true
    "aba" --> false
    "moOse" --> false (ignore letter case)
    """
    if (len(string) == len(set(string.lower()))):
        print('its okay')
        return True
    else:
        print('something going wrong')
        return False

# v2


def is_isogram_v2(string):
    return len(string) == len(set(string.lower()))


string = "Dermatoglyphics"
is_isogram(string)
is_isogram_v2(string)
