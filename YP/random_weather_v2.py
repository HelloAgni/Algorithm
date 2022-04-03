def random_weather(temp):
    """
    Назовём хаотичностью погоды за n дней количество дней, в которые
    температура строго больше, чем в день до и в день после текущего.
    Выведите единственное число — хаотичность за данный период.
    """
    print(temp)
    random_weather = 0
    for i in range(1, n + 1):
        if (temp[i-1] is None or temp[i-1] < temp[i]) and (
            temp[i+1] is None or temp[i] > temp[i+1]
        ):
            random_weather += 1
    print(random_weather)


if __name__ == '__main__':
    n = int(input())
    temp = [None, *map(int, input().split()), None]
    random_weather(temp)
