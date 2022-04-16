import sys


class ListQueue:
    """
    Очередь написанная с использованием связного списка
    должна поддерживать выполнение трёх команд:
    get() — вывести элемент, находящийся в голове очереди,
    и удалить его. Если очередь пуста, то вывести «error».
    put(x) — добавить число x в очередь
    size() — вывести текущий размер очереди
    """
    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)

    def get(self):
        if len(self.queue) == 0:
            return 'error'
        return self.queue.pop(0)  # first in first out

    def size(self):
        return len(self.queue)

    def __str__(self):
        return f'SQ = {self.queue}'


if __name__ == '__main__':
    n = int(input())  # количество команд
    q = ListQueue()
    new = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        if 'put' in line.split():
            q.put(int(line.split()[-1]))
        if 'get' in line.split():
            p = q.get()
            if p == 'error':
                new.append('error')
            else:
                new.append(p)
        if 'size' in line.split():
            new.append(q.size())
    print(*new, sep='\n')
