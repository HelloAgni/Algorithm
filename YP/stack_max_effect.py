import sys


class StackMaxEffective:
    """
    Реализуйте класс StackMaxEffective, поддерживающий операцию
    определения максимума среди элементов в стеке.
    Сложность операции должна быть O(1).
    Если стек пустой, для команды get_max() напечатайте «None».
    Если происходит удаление из пустого стека — напечатайте «error».
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        if self.items:
            new_max = max(item, self.items[-1][1])
        else:
            new_max = item
        self.items.append((item, new_max))

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return 'error'

    def get_max(self):
        return self.items[-1][1]

    def __str__(self):
        return f'SM = {self.items}'


if __name__ == '__main__':
    n = int(input())  # количество команд
    s = StackMaxEffective()
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
