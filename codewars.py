from collections import Counter


def count(array):
    """
    Write a function that takes an array
    and counts the number of each unique element present.
    count(['james', 'james', 'john'])
    { 'james' => 2, 'john' => 1}
    """
    unique = dict(zip(array, (array.count(i) for i in array)))
    print(unique)


# v2
def count_v2(array):
    x = Counter(array)
    print(dict(x))


array = ['a', 'a', 'b', 'b', 'b']  # { 'a': 2, 'b': 3 }
count(array)
count_v2(array)
