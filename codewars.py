def invert(lst):
    """
    Given a set of numbers, return the additive inverse of each.
    Each positive becomes negatives, and the negatives become positives.
    Example:
    invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
    invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
    invert([]) == []
    """
    new = []
    for x in lst:
        new.append(-1*x)
    print(new)

# v2


def invert_v2(lst):
    print([-x for x in lst])


lst = [1, 2, 3, 4, 5]
invert(lst)
invert_v2(lst)
