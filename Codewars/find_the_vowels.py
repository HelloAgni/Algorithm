def vowel_indices(word):
    """
    Find the index of the vowels in a given word,
    Vowels in this context refers to: a e i o u y (including upper case)
    This is indexed from [1..n] (not zero indexed!)
    Some examples:
    Mmmm  => []
    Super => [2,4]
    Apple => [1,5]
    YoMama -> [1,2,4,6]
    """
    new = []
    vowels = 'aeiouy'
    for c, x in enumerate(word):
        if x in vowels or x in vowels.upper():
            new.append(c+1)
    return new


def vowel_indices_v2(word):
    vowels = 'aeiouy'
    return [c + 1 for c, x in enumerate(word)
            if x in vowels or x in vowels.upper()]


print(vowel_indices('Apple'))
print(vowel_indices_v2('YoMama'))
