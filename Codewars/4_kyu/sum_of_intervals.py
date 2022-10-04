from timeit import timeit


def sum_of_intervals(intervals):
    """
    Write a function that accepts an array of intervals,
    and returns the sum of all the interval lengths.
    Overlapping intervals should only be counted once.
    """
    intervals = list(map(list, sorted(intervals)))
    new = [intervals[0]]
    c = 0
    for x in intervals:
        start, end = x
        if start > new[c][1]:
            c += 1
            new.append([start, end])
        elif end > new[c][1]:
            new[c][1] = end
    return sum([end-start for start, end in new])


a = [  # => 19 [[1,5],[1,6],[5,11],[10,20],[16,19]]
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11],
]
b = [  # => 7
    [1, 4],
    [7, 10],
    [3, 5]
    ]
c = [  # => 7
    (1, 4),
    (7, 10),
    (3, 5)
]
for x in [a, b, c]:
    print('Ok =>', sum_of_intervals(x))

check_1 = """
def sum_of_intervals(intervals):
    intervals = list(map(list, sorted(intervals)))
    new = [intervals[0]]
    c = 0
    for x in intervals:
        start, end = x
        if start > new[c][1]:
            c += 1
            new.append([start, end])
        elif end > new[c][1]:
            new[c][1] = end
    return sum([end-start for start, end in new])
a = [  # => 100000030
    [0, 20],
    [-100000000, 10],
    [30, 40]
] 
sum_of_intervals(a)
"""
print(timeit(check_1))
