from collections import Counter


def move_zeros(array):
    """
    Write an algorithm that takes an array and moves all of the zeros
    to the end, preserving the order of the other elements.
    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
    """
    st = ''.join([str(x) for x in array])
    c = st.count('0')
    new_st = st.replace('0', '')
    return [int(x) for x in new_st] + [0] * c


def move_zeros_v2(array):
    st = ''.join([str(x) for x in array])
    c = Counter(array)[0]
    new_st = st.replace('0', '')
    return [int(x) for x in new_st] + [0] * c


array = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]  # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
print(move_zeros(array))
print(move_zeros_v2(array))
