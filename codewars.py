def to_float_array(arr):
    """
    Create the function that takes as a parameter a sequence of numbers
    represented as strings and outputs a sequence of numbers.
    Example:["1", "2", "3"] to [1, 2, 3]
    Note that you can receive floats as well.
    """
    new = []
    for x in arr:
        new.append(float(x))
    print(new)


# v2

def to_float_array_v2(arr):
    print(list(map(float, arr)))


arr = ["1", "2", "3"]
to_float_array(arr)
to_float_array_v2(arr)
