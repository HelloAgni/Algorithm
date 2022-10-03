from collections import Counter


def number_of_pairs(gloves):
    """
    Given an array describing the color of each glove,
    return the number of pairs you can constitute,
    assuming that only gloves of the same color can form pairs.
    Examples:
    input = ["red", "green", "red", "blue", "blue"]
    result = 2 (1 red pair + 1 blue pair)
    """
    count = 0
    gloves = Counter(gloves)
    for x in gloves.values():
        count += x // 2
    return count


def number_of_pairs_v2(gloves):
    return sum([x // 2 for x in Counter(gloves).values()])


gloves = [
    "red", "green", "blue", "blue", "red", "green", "red", "red", "red"]  # 4
print(number_of_pairs(gloves))
print(number_of_pairs_v2(gloves))
