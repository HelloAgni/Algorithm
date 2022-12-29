def power_sumDigTerm(n):
    """
    The number 81 has a special property, a certain power of the sum
    of its digits is equal to 81 (nine squared). Eighty one (81),
    is the first number in having this property
    (not considering numbers of one digit). The next one,
    is 512. Let's see both cases with the details
    8 + 1 = 9 and 92 = 81
    512 = 5 + 1 + 2 = 8 and 83 = 512
    """
    new = []
    for i in range(2, 100):
        for j in range(2, 50):
            pow = i ** j
            if sum([int(x) for x in str(pow)]) == i:
                new.append(pow)
    new.sort()
    return new[n-1]


n = 5
n_1 = 15
print(power_sumDigTerm(n))
print(power_sumDigTerm(n_1))
