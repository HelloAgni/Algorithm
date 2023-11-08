"""
Given an array representing a series of floors you must reach by elevator,
return an integer representing the total distance travelled
for visiting each floor in the array in order.

// simple examples
elevatorDistance([5,2,8]) = 9
elevatorDistance([1,2,3]) = 2
elevatorDistance([7,1,7,1]) = 18
"""


def elevator_distance(array):
    # your code here
    return sum([abs(array[x] - array[x + 1]) for x in range(len(array) - 1)])


array = [7, 1, 7, 1]
print(elevator_distance(array))
