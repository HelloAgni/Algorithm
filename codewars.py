def over_the_road(address, n):
    """
    You would like to find out the house number of the people
    on the other side of the street.
    Example (address, n --> output)
    Given your house number address and length of street n,
    give the house number on the opposite side of the street.
    1, 3 --> 6      Street:     1|   |8
    3, 3 --> 4                  3|   |6
    2, 3 --> 5                  5|   |4
    3, 5 --> 8                  7|   |2
    """
    print((n*2) - address + 1)

# v2


address = 1  # 5
n = 1
over_the_road(address, n)
