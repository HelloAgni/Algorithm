import sys


class Deck:
    """
    Реализовать структуру данных Дек,
    максимальный размер которого определяется заданным числом.
    При реализации используйте кольцевой буфер.
    push_back(value) – добавить элемент в конец дека.
    push_front(value) – добавить элемент в начало дека.
    Если в деке уже находится максимальное число элементов, вывести «error».
    pop_front() – вывести первый элемент дека и удалить его.
    pop_back() – вывести последний элемент дека и удалить его.
    Если дек был пуст, то вывести «error».
    """
    def __init__(self, max):
        self.deck = [None] * max
        self.max = max
        self.head = 0
        self.tail = 0
        self.size_deck = 0

    def push_back(self, value):
        if self.size_deck != self.max:
            self.deck[self.tail] = value
            self.tail = (self.tail + 1) % self.max
            self.size_deck += 1
        else:
            print('error')

    def push_front(self, value):
        if self.size_deck != self.max:
            self.head = (self.head - 1) % self.max
            self.deck[self.head] = value
            self.size_deck += 1
        else:
            print('error')

    def pop_back(self):
        if self.size_deck == 0:
            return 'error'
        self.tail = (self.tail - 1) % self.max
        x = self.deck[self.tail]
        self.deck[self.tail] = None
        self.size_deck -= 1
        return x

    def pop_front(self):
        if self.size_deck == 0:
            return 'error'
        x = self.deck[self.head]
        self.deck[self.head] = None
        self.head = (self.head + 1) % self.max
        self.size_deck -= 1
        return x

    def size(self):
        pass


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    deck = Deck(m)
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        command = line.split()
        if 'push_back' in command:
            deck.push_back(command[1])
        if 'push_front' in line.split():
            deck.push_front(command[1])
        if 'pop_back' in command:
            print(deck.pop_back())
        if 'pop_front' in command:
            print(deck.pop_front())
