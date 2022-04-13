import sys


class StackMax:
    """
    Нужно реализовать класс StackMax, который поддерживает операцию
    определения максимума среди всех элементов в стеке.
    Класс должен поддерживать операции push(x),
    где x – целое число, pop() и get_max().
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return 'error'

    def get_max(self):
        return (max(self.items))

    def __str__(self):
        return f'SM = {self.items}'


if __name__ == '__main__':
    n = int(input())  # количество команд
    s = StackMax()
    new = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        if 'push' in line.split():
            s.push(int(line.split()[-1]))
        if 'get_max' in line.split():
            if len(s.items) == 0:
                new.append(None)
            else:
                new.append(s.get_max())
        if 'pop' in line.split():
            if s.pop() == 'error':
                new.append('error')
    print(*new, sep='\n')
