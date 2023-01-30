def split_the_bill(x):
    """
    Function should return an object/dict with the same names,
    showing how much money the members should pay or receive.
    3 friends go out together: A spends £20, B spends £15, and C spends £10.
    The function should return an object/dict showing that
    A should receive £5, B should receive £0, and C should pay £5.
    """
    avg = sum(x.values()) / len(x.values())
    return {k: round(v - avg, 2) for k, v in x.items()}


group = {
    'A': 20,
    'B': 15,
    'C': 10
}
print(split_the_bill(group))  # {'A': 5, 'B': 0, 'C': -5}

group_1 = {
    'A': -17.200000000000003,
    'B': -32.2,
    'C': -47.2,
    'D': 95.8,
    'E': 0.7999999999999972}
print(split_the_bill(group_1))
# {'A': -17.2, 'B': -32.2, 'C': -47.2, 'D': 95.8, 'E': 0.8}
