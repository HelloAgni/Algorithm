import sys


class MaxItemsError(Exception):
    """Достигнуто макимальное число элементов."""

    pass


class ZeroItemsError(Exception):
    """Отсутствуют элементы для удаления."""

    pass


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
        self.__items = [None] * max
        self.__max = max
        self.__head = 0
        self.__tail = 0
        self.__size_deck = 0

    def push_back(self, value):
        if self.__size_deck != self.__max:
            self.__items[self.__tail] = value
            self.__tail = (self.__tail + 1) % self.__max
            self.__size_deck += 1
        else:
            raise MaxItemsError

    def push_front(self, value):
        if self.__size_deck != self.__max:
            self.__head = (self.__head - 1) % self.__max
            self.__items[self.__head] = value
            self.__size_deck += 1
        else:
            raise MaxItemsError

    def pop_back(self):
        if self.__size_deck == 0:
            raise ZeroItemsError
        self.__tail = (self.__tail - 1) % self.__max
        x = self.__items[self.__tail]
        self.__items[self.__tail] = None
        self.__size_deck -= 1
        return x

    def pop_front(self):
        if self.__size_deck == 0:
            raise ZeroItemsError
        x = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__head = (self.__head + 1) % self.__max
        self.__size_deck -= 1
        return x

    def size(self):
        pass


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    deck = Deck(m)
    for _ in range(n):
        try:
            line = sys.stdin.readline().rstrip()
            command = line.split()
            if len(command) > 1:
                getattr(deck, command[0])(command[1])
            else:
                print(getattr(deck, command[0])())
        except MaxItemsError:
            print('error')
        except ZeroItemsError:
            print('error')
