# Дана матрица. Нужно написать функцию,
# которая для элемента возвращает всех его соседей.
import sys

n = int(input('Количество строк: '))  # количество строк
m = int(input('Количество столбцов: '))  # количество столбцов
output_numbers = []
for i in range(n):
    line = sys.stdin.readline().rstrip()
    output_numbers.append(line.split(' '))
x = int(input('Ряд/строка с 0: '))  # координаты по вертикали (начиная с 0)
y = int(input('Столбец с 0:'))  # координаты по горизонтали (начиная с 0)
print(output_numbers)
print(output_numbers[x][y])
if n == 1 and m == 1:
    print(' ')
elif n == 1 and m == 2:
    print(output_numbers[x][y+1])
    print('1')
elif n == 2 and m == 1:
    print('2')
    print(output_numbers[x+1][y])
elif n > 2 and m == 1:
    print('21')
    print(output_numbers[x+1][y], output_numbers[x-1][y])
elif (n == 1 and m > 2 and output_numbers[x][y] == output_numbers[0][y]
        and output_numbers[x][y] != output_numbers[0][-1]):
    print('3')
    print(' '.join(sorted((output_numbers[x][y-1], output_numbers[x][y+1]))))
elif output_numbers[x][y] == output_numbers[0][0]:
    print('нулевой элемент')
    print(f'Правый - {output_numbers[x][y+1]}, Нижний - {output_numbers[x+1][y]}')
elif n == 1 and m > 2 and output_numbers[x][y] == output_numbers[0][-1]:
    print('последний элемент в 0 строке')
    print(f'Левый - {output_numbers[x][y-1]}')
elif output_numbers[x][y] == output_numbers[0][-1]:
    print('последний элемент в 0 строке')
    print(f'Левый - {output_numbers[x][y-1]}, Нижний - {output_numbers[x+1][y]}')
elif output_numbers[x][y] == output_numbers[-1][0]:
    print('0 элемент в последней строке')
    print(f'Правый - {output_numbers[x][y+1]}, Верхний - {output_numbers[x-1][y]}')
elif output_numbers[x][y] == output_numbers[-1][-1]:
    print('последний элемент')
    print(f'Левый - {output_numbers[x][y-1]}, Верхний - {output_numbers[x-1][y]}')
elif output_numbers[x][y] == output_numbers[0][y]:
    print('0 строка не с краю')
    print(f'Левый - {output_numbers[x][y-1]},'
          f'Правый - {output_numbers[x][y+1]}, Нижний - {output_numbers[x+1][y]}')
elif output_numbers[x][y] == output_numbers[-1][y]:
    print('последняя строка не с краю')
    print(f'Левый - {output_numbers[x][y-1]},'
          f'Правый - {output_numbers[x][y+1]}, Верхний - {output_numbers[x-1][y]}')
elif output_numbers[x][y] == output_numbers[x][0]:
    print('1ый столбец не с краю')
    print(f'Правый - {output_numbers[x][y+1]}'
          f'Верхний - {output_numbers[x-1][y]}, Нижний - {output_numbers[x+1][y]}')
elif output_numbers[x][y] == output_numbers[x][-1]:
    print('последний столбец не с краю')
    print(f'Левый - {output_numbers[x][y-1]}'
          f'Верхний - {output_numbers[x-1][y]}, Нижний - {output_numbers[x+1][y]}')
else:
    print(f'Левый - {output_numbers[x][y-1]}, Правый - {output_numbers[x][y+1]}')
    print(f'Верхний - {output_numbers[x-1][y]}, Нижний - {output_numbers[x+1][y]}')
