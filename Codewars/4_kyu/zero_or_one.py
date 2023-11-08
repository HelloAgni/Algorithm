"""
You are given an odd integer n and a two-dimensional array s,
which contains n equal-sized arrays of 0s and 1s.

Return an array of the same length as the elements of n,
such that its ith element is the one that appears most
frequently at the ith position of s' elements.

Code Limit
Less than 55 characters
"""
# zero_or_one=lambda n,s:[sum(x)>n/2for x in zip(*s)] -> correct solution

zero_or_one = lambda n, s: [round(sum(x)/n) for x in zip(*s)]
n = 3
s = [[1, 0, 1, 0, 1], [1, 1, 1, 0, 1], [0, 1, 1, 1, 0]]
print(zero_or_one(n, s))