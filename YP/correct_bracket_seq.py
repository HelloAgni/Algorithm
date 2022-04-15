def is_correct_bracket_seq(line):
    """
    На вход подаётся последовательность из скобок трёх видов: [], (), {}.
    Напишите функцию которая принимает на вход скобочную
    последовательность и возвращает True,
    если последовательность правильная, а иначе False.
    """
    bracket = ['(', '[', '{']
    stack = []  # last in first out
    for x in line:
        if x in bracket:
            stack.append(x)
        elif x == ')' and len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        elif x == ']' and len(stack) != 0 and stack[-1] == '[':
            stack.pop()
        elif x == '}' and len(stack) != 0 and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(x)
    if stack:
        return False
    else:
        return True


if __name__ == '__main__':
    line = input()
    bracket_seq = is_correct_bracket_seq(line)
    print(bracket_seq)
