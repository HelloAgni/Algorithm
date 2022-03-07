def count_by(x, n):
    """
    Create a function with two arguments that
    will return an array of the first (n) multiples of (x)...
    Examples:
    count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
    count_by(2,5) #should return [2,4,6,8,10]
    """
    new = []
    for g in range(1, n+1):
        new.append(g*x)
    print(new)

# v2


def count_by_v2(x, n):
    print([i * x for i in range(1, n+1)])


x = 1
n = 10
count_by(x, n)
count_by_v2(x, n)
