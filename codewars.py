# Example [1,-4,7,12] => 1 + 7 + 12 = 20

def positive_sum(arr):
    # Your code here
    sum = 0
    for x in arr:
        if x > 0:
            sum += x
    # return sum
    print(sum)


arr = [1, -4, 7, 12]

positive_sum(arr)
