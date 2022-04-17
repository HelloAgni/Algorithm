def palindrome_rec(string):
    """
    Палиндром с рекурсией...Пример. But memory out!!!
    Выведите «True», если фраза является палиндромом,
    и «False», если не является.
    """
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome_rec(string[1:-1])


if __name__ == '__main__':
    string = input().lower()
    string = ''.join(x for x in string if x.isalpha())
    print(palindrome_rec(string))
