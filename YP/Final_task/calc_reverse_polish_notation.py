class Stack:
    """
    В единственной строке дано выражение,
    записанное в обратной польской нотации.
    Числа и арифметические операции записаны через пробел.
    На вход могут подаваться операции: +, -, *, / и числа,
    по модулю не превосходящие 10000.
    Выведите единственное число — значение выражения.
    """
    def __init__(self):
        self.__items = []
        self.__operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y,
            }
        self.__count = 0

    def push(self, line):
        for i in line:
            if i in self.__operations:
                self.__items[self.__count - 2] = self.__operations[i](
                    self.__items[self.__count - 2],
                    self.__items[self.__count - 1]
                )
                self.__count -= 1
                self.pop()
            if i not in self.__operations:
                self.__items.append(i)
                self.__count += 1
        return self.__items[-1]

    def pop(self):
        if len(self.__items) != 0:
            self.__items.pop()
        else:
            return 'error'


if __name__ == '__main__':
    calculations = Stack()
    line = [int(x) if x not in calculations._Stack__operations
            else x for x in input().split()]
    result = calculations.push(line)
    print(result)
