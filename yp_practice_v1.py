n = int(input())  # количество строк
temp = list(map(int, (input().split(maxsplit=n-1))))
count = 0
if n == 1:
    count += 1
if len(temp) == 2 and temp[0] > temp[1]:
    count += 1
if len(temp) == 2 and temp[1] > temp[0]:
    count += 1
if len(temp) > 2 and temp[-1] > temp[-2]:
    count += 1
if len(temp) > 2 and temp[0] > temp[1]:
    count += 1
if len(temp) > 2:
    for i in range(1, len(temp)-1):
        if temp[i-1] < temp[i] > temp[i+1]:
            count += 1
print(count)
