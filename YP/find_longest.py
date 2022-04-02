def find_longest(string):
    """
    В первой строке выведите самое длинное слово.
    Во второй строке выведите его длину. Если подходящих слов несколько,
    выведите то, которое встречается раньше.
    """
    s = string.split(' ')
    m = max(s, key=len)
    print(m, len(m), sep='\n')


if __name__ == '__main__':
    n = int(input())
    string = input()
    find_longest(string)