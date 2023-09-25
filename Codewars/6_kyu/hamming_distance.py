"""
Complete the function so that it returns the number
of positions where the input strings do not match.

a = "I like turtles"
b = "I like turkeys"
Result: 3

a = "Hello World"
b = "Hello World"
Result: 0
"""


def hamming(a, b):
    return sum(el1 != el2 for el1, el2 in zip(a, b))


a = "I like turtles"
b = "I like turkeys"
print(hamming(a, b))
