def combinations(n, buttons):
    """
    Известно в каком порядке были нажаты кнопки телефона, без учета повторов.
    Напечатайте все комбинации букв,
    которые можно набрать такой последовательностью нажатий.
    """
    if n == '':
        return ['']
    new = []
    # s = numbers[n[-1]]
    for i in combinations(n[:-1:], buttons):
        for x in buttons[n[-1]]:
            new.append(i + x)
    return new


if __name__ == '__main__':
    n = input()
    buttons = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    result = combinations(n, buttons)
    print(*result)
