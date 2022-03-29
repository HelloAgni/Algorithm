def moving_average(timeseries, k):
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(timeseries[0:k])
    result.append(current_sum / k)
    for i in range(0, len(timeseries) - k):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+k]
        current_avg = current_sum / k
        result.append(current_avg)
    print(*result)
    return result


n = int(input())
timeseries = list(map(int, input().split()))
k = int(input())
moving_average(timeseries, k)
