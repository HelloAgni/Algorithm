class Calculator:
    """
    В единственной строке дано выражение,
    записанное в обратной польской нотации.
    Числа и арифметические операции записаны через пробел.
    На вход могут подаваться операции: +, -, *, / и числа,
    по модулю не превосходящие 10000.
    Выведите единственное число — значение выражения.
    """
    def __init__(self):
        self.items = []
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y,
            }
        self.count = 0

    def push(self, line):
        for i in line:
            if i in self.operations:
                self.items[self.count - 2] = self.operations[i](
                    self.items[self.count - 2], self.items[self.count - 1]
                )
                self.count -= 1
                self.items.pop()
            if i not in self.operations:
                self.items.append(i)
                self.count += 1
        return self.items[-1]


if __name__ == '__main__':
    calculations = Calculator()
    line = [int(x) if x not in calculations.operations
            else x for x in input().split()]
    result = calculations.push(line)
    print(result)
