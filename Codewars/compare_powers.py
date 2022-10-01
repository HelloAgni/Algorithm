def compare_powers(n1, n2):
    """
     Build a function to compare powers,
     returning -1 if the first member is larger,
     0 if they are equal,
     1 otherwise
    compare_powers([2,10],[3,10])==1
    compare_powers([2,10],[2,10])==0
    compare_powers([3,9],[5,6])==-1
    """
    n1[-1] = n1[-1] / n2[-1]
    n2[-1] = 1
    if pow(n1[0], n1[-1]) > pow(n2[0], n2[-1]):
        return -1
    elif pow(n1[0], n1[-1]) < pow(n2[0], n2[-1]):
        return 1
    else:
        return 0


a = [1594, 9655]
b = [2398, 8468]
print(compare_powers(a, b))
