def find_short(s):
    """
    Simple, given a string of words, return the length of the shortest word(s).
    """
    word = s.split(' ')
    print(word)
    word.sort(key=len)
    print(len(word[0]))


s = "Let's travel abroad shall we"
find_short(s)
