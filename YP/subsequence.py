def subsequence(s, t):
    """
    Выведите True, если s является подпоследовательностью t, иначе —– False.
    """
    if s == '':
        return True
    i = 0
    for x in range(len(t)):
        if s[i] == t[x]:
            i += 1
        if i == len(s):
            return True
    return False


if __name__ == '__main__':
    s = input()
    t = input()
    result = subsequence(s, t)
    print(result)
