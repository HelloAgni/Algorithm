def moving_average(timeseries, k):
    result = []
    sum1 = sum(timeseries[0:k])
    result.append(sum1/k)
    if len(timeseries) > k:
        for i in range(1, n - k + 1):
            sum1 = sum1 - timeseries[i - 1] + timeseries[i - 1 + k]
            result.append(sum1 / k)
    print(*result)
    return result


n = int(input())
timeseries = list(map(int, input().split()))
k = int(input())
moving_average(timeseries, k)
