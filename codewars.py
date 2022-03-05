# For example, the string
# "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
import re

string_ = 'This website is for losers LOL!'


def disemvowel(string_):
    string_ = re.sub(r'[AEIOU]', '', string_, flags=re.IGNORECASE)
    # return string_
    print(string_)


disemvowel(string_)

# v2


def disemvowel_v2(string_):
    vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    string_ = (string_.translate({ord(x): None for x in vowel}))
    # return string_
    print(string_)


disemvowel_v2(string_)
