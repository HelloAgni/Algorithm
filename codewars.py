from heapq import nlargest, nsmallest


def sum_two_smallest_numbers(numbers):
    """
    For example,
    when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
    [10, 343445353, 3453445, 3453545353453] should return 3453455.
    """
    mini = nsmallest(2, numbers)
    maxi = nlargest(2, numbers)
    print(sum(mini))
    print(sum(maxi))


numbers = [19, 0, 42, 0, 77]
sum_two_smallest_numbers(numbers)
