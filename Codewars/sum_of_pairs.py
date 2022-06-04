def sum_pairs(ints, s):
    """
    Given a list of integers and a single sum value,
    return the first two values (parse from the left please)
    in order of appearance that add up to form the sum.
    sum_pairs([4, 3, 2, 3, 4], 6)
        ^-----^         4 + 2 = 6, indices: 0, 2 *
        ^-----^      3 + 3 = 6, indices: 1, 3
        ^-----^   2 + 4 = 6, indices: 2, 4
    * entire pair is earlier, and therefore is the correct answer
    == [4, 2]
    """
    cache = {}
    for i in ints:
        if s - i in cache:
            return [s - i, i]
        cache[i] = i


def sum_pairs_v2(ints, s):
    cache = set()
    for i in ints:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


def test():
    l1 = [10, 5, 2, 3, 7, 5]
    s1 = 10
    result1 = sum_pairs(l1, s1) == [3, 7]
    l2 = [4, 3, 2, 3, 4]
    s2 = 6
    result2 = sum_pairs(l2, s2) == [4, 2]
    l3 = [11, 3, 7, 5]
    s3 = 10
    result3 = sum_pairs(l3, s3) == [3, 7]
    l4 = [4, 3, 2, 3, 4]
    s4 = 6
    result4 = sum_pairs_v2(l4, s4) == [4, 2]
    return result1, result2, result3, result4


print(test())
