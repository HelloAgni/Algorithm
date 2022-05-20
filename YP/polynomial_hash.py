def polynomial_hash(string, a, m):
    """
    Написать функцию, вычисляющую хеш строки s.
    В данной задаче необходимо использовать в качестве значений
    отдельных символов их коды в таблице ASCII.
    Полиномиальный хеш.
    """
    n = len(string)
    current_hash = {}
    if n < 100:
        result = 0
        for count, elem in enumerate(string):
            if elem in current_hash:
                result += current_hash[elem] * a ** (n - 1 - count)
            else:
                current_hash[elem] = ord(elem)
                result += current_hash[elem] * a ** (n - 1 - count)
        return result % m
    if n > 100:  # метод Горнера
        string = string[::-1]
        x = 1
        result = 0
        for elem in string:
            if elem in current_hash:
                result = (result + current_hash[elem] * x) % m
                x = (x * a) % m
            else:
                current_hash[elem] = ord(elem)
                result = (result + ord(elem) * x) % m
                x = (x * a) % m
        return result


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    string = input()
    result = polynomial_hash(string, a, m)
    print(result)
