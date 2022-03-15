def nb_dig(n, d):
    """
    Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.
    Square all numbers k (0 <= k <= n) between 0 and n.
    Count the numbers of digits d used in the writing of all the k**2.
    Call nb_dig (or nbDig or ...) the function taking n
    and d as parameters and returning this count.
    Examples:
    n = 10, d = 1
    the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
    We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.
    """
    s = str([k*k for k in range(n+1)])
    total = ''.join(s).count(str(d))
    print(total)

# v2


def nb_dig_v2(n, d):
    print(sum(str(i*i).count(str(d)) for i in range(n+1)))


n = 10
d = 1
nb_dig(n, d)
nb_dig_v2(n, d)
