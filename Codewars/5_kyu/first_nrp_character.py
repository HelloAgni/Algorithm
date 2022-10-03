def first_non_repeating_letter(string):
    """
    Write a function that takes a string input, and returns
    the first character that is not repeated anywhere in the string.
    'stress', the function should return 't'
    'sTreSS' should return 'T'
    """
    for x in string:
        if string.lower().count(x.lower()) == 1:
            return x
    return ''


s_1 = 'sTreSS'  # T
s_2 = 'stress'  # t
print(
    first_non_repeating_letter(s_1),
    first_non_repeating_letter(s_2)
)
