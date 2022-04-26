def bracket_binary_gen(n, counter_open, counter_close, line):
    """
    Функция должна напечатать все возможные скобочные последовательности (ПСП)
    заданной длины в алфавитном (лексикографическом) порядке.
    """
    if counter_open + counter_close == 2 * n:
        print(line)
    if counter_open < n:
        bracket_binary_gen(n, counter_open + 1, counter_close, line + '(')
    if counter_open > counter_close:
        bracket_binary_gen(n, counter_open, counter_close + 1, line + ')')


if __name__ == '__main__':
    n = int(input())  # количество парных скобок
    result = bracket_binary_gen(n, counter_open=0, counter_close=0, line='')
