from collections import Counter


def solve(arr):
    """
    Sort elements in an array by decreasing frequency of elements.
    If two elements have the same frequency, sort them by increasing value.
    solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
    """
    new = Counter(arr)
    return sorted(arr, key=lambda x: (-new[x], x))


def solve_v2(arr):
    return sorted(sorted(arr), key=lambda n: arr.count(n), reverse=True)


arr = [5, 9, 6, 9, 6, 5, 9, 9, 4, 4]  # [9, 9, 9, 9, 4, 4, 5, 5, 6, 6]
print(solve(arr))
print(solve_v2(arr))
