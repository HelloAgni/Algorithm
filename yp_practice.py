# ex_1
import sys

a = int(input())
b = int(input())
sys.stdin.readline()
print(a + b)


# ex_2
n = int(input())
a = map(int, input().split(maxsplit=n))
b = map(int, input().split(maxsplit=n))

for z, x in zip(a, b):
    print(z, x, end=' ')


# test

# n = int(input())
# arr = list(map(int, input().split()))
# print(" ".join(list(map(str, arr))))
