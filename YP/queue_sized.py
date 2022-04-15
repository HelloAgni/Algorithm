import sys


class MyQueueSized:
    """
    Нужно реализовать класс MyQueueSized, который принимает параметр max_size,
    означающий максимально допустимое количество элементов в очереди.
    При превышении допустимого размера очереди нужно вывести «error».
    При вызове операций pop() или peek() для пустой очереди
    нужно вывести «None».
    """
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)  # first in first out

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def __str__(self):
        return f'SQ = {self.queue}'


if __name__ == '__main__':
    n = int(input())  # количество команд
    max_size = int(input())  # размер очереди
    q = MyQueueSized()
    new = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        if 'push' in line.split():
            q.push(int(line.split()[-1]))
            if q.size() > max_size:
                new.append('error')
                q.queue.pop()
        if 'pop' in line.split():
            p = q.pop()
            if p is None:
                new.append(None)
            else:
                new.append(p)
        if 'size' in line.split():
            new.append(q.size())
        if 'peek' in line.split():
            if q.peek() is None:
                new.append(None)
            else:
                new.append(q.peek())
    print(*new, sep='\n')
