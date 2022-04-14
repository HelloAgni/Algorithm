def is_correct_bracket_seq(n):
    """
    На вход подаётся последовательность из скобок трёх видов: [], (), {}.
    Напишите функцию которая принимает на вход скобочную
    последовательность и возвращает True,
    если последовательность правильная, а иначе False.
    """
    while '()' in n or '[]' in n or '{}' in n:
        n = n.replace('()', '')
        n = n.replace('[]', '')
        n = n.replace('{}', '')
    return not n


if __name__ == '__main__':
    n = input()
    bracket_seq = is_correct_bracket_seq(n)
    print(bracket_seq)
