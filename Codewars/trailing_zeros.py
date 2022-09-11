import time
from math import factorial


def zeros(n):
    """
    Write a program that will calculate the number of trailing zeros
    in a factorial of a given number.
    zeros(12) = 2
    12! = 479001600 --> 2 trailing zeros

    ***Clue for solution***
    Each multiple of 5^1 adds a 0
    Each multiple of 5^2 adds a 0
    Each multiple of 5^3 adds a 0...
    """
    i = 5
    count = 0
    while n >= i:
        count += n // i
        i *= 5
    return count


def zeros_v2(n):
    """Slow solution, but obvious"""
    count = 0
    a = factorial(n)
    while a % 10 == 0:
        count += 1
        a = a // 10
    return count


start_time = time.time()
num = 10000
print(zeros(num))
run_time = time.time() - start_time
start_time = time.time()
print(zeros_v2(num))
run_time_v2 = time.time() - start_time
print(f'Функция zeros выполнена за {run_time:.7f} c.\n'
      f'Функция zeros_v2 выполнена за {run_time_v2:.7f} c.')
