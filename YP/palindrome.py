import re


def palindrome(string):
    """
    Выведите «True», если фраза является палиндромом,
    и «False», если не является.
    """
    s = re.sub(r'\W', '', string.lower())
    r = s[::-1]
    if s == r:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    string = input()
    palindrome(string)
