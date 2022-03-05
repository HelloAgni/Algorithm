def abbrev_name(name):
    """
    Write a function to convert a name into initials.
    Str takes two words with one space in between them.
    Sam Harris => S.H
    patrick feeney => P.F
    """
    x = name.split()
    abrev = []
    for first in x:
        abrev.append(first[0])
    s = '.'.join(abrev)
    print(s.upper())


name = 'sam Harris'
abbrev_name(name)


# v2

def abbrev_name_v2(name):
    print('.'.join(x[0] for x in name.split()).upper())


name = 'Poll Harris'
abbrev_name_v2(name)
