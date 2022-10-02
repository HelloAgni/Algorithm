import timeit


def anagrams(word, words):
    """
    Write a function that will find all the anagrams of a word from a list.
    You will be given two inputs a word and an array with words.
    You should return an array of all the anagrams or
    an empty array if there are none. For example:
    anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
    => ['carer', 'racer']
    """
    return [x for x in words if sorted(x) == sorted(word)]


w_1 = 'abba'
ar_1 = ['aabb', 'abcd', 'bbaa', 'dada']  # => ['aabb', 'bbaa']
w_2 = 'racer'
ar_2 = ['crazer', 'carer', 'racar', 'caers', 'racer']  # => ['carer', 'racer']
w_3 = 'laser'
ar_3 = ['lazing', 'lazy',  'lacer']  # => []
print(anagrams(w_1, ar_1))
print(anagrams(w_2, ar_2))
print(anagrams(w_3, ar_3))

check = """
def anagrams(word, words):
    return [x for x in words if sorted(x) == sorted(word)]
word = 'racer'
words = ['crazer', 'carer', 'racar', 'caers', 'racer']
anagrams(word, words)
    """
print(timeit.timeit(check))
