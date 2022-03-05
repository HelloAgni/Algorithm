import time


def binary_serch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(binary_serch(my_list, 12))

start_time = time.time()
binary_serch(my_list, 9)
print("--- %s seconds ---" % (time.time() - start_time))

# $ python -m cProfile test1.py
