import re


def perfect_square(square):

    """
    Write function which validates an input string.
    If the string is a perfect square return true,false otherwise.
    Perfect squares must have same width and height -> cpt.Obvious
    perfectSquare = "...\n...\n...";
       `...
        ...
        ...`
    notPerfect = "..,\n..\n...";
    `..,
     ..
     ...`
    """
    check_elements = re.sub(r'[.\n]', '', square)
    if check_elements:
        return False
    sq = square.split('\n')
    if len(set(sq)) == 1:
        return len(sq[0]) == len(sq)
    return False


s = '.'
print(perfect_square(s))  # True
s_1 = "...\n..\n."
print(perfect_square(s_1))  # False
s_2 = "...\n...\n..."
print(perfect_square(s_2))  # True
s_3 = "..,\n..\n..."
print(perfect_square(s_3))  # False
s_4 = '---\n---\n---'
print(perfect_square(s_4))  # False
s_5 = '.\n.\n.\n.'
print(perfect_square(s_5))  # False
