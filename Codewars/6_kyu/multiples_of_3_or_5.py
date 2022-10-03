def solution(number):
    """
    Finish the solution so that it returns the sum of all the multiples
    of 3 or 5below the number passed in.
    Additionally, if the number is negative,
    return 0 (for languages that do have them).
    """
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])


number = 10  # [3, 5, 6, 9] => 23
print(solution(number))
