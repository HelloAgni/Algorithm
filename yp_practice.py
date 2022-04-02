# Дана матрица. Нужно написать функцию,
# которая для элемента возвращает всех его соседей.
import sys

n = int(input())  # количество строк
m = int(input())  # количество столбцов
output_numbers = []
for i in range(n):
    line = sys.stdin.readline().rstrip()
    output_numbers.append(line.split(' '))
x = int(input())  # координаты по вертикали (начиная с 0)
y = int(input())  # координаты по горизонтали (начиная с 0)
if n == 1 and m == 1:
    print(' ')
elif 2 >= n > 1 and m == 1:
    print(output_numbers[x+1][y])
elif n == 1 and 2 >= m > 1:
    print(output_numbers[x][y+1])
elif n == 1 and m > 2 and output_numbers[x][y] == output_numbers[0][y]:
    print(' '.join(sorted((output_numbers[x][y-1], output_numbers[x][y+1]))))
# elif output_numbers[x][y] == output_numbers[0][0]:
#     print(' '.join(sorted((output_numbers[x][y+1], output_numbers[x+1][y]))))
elif output_numbers[x][y] == output_numbers[0][-1]:
    print(' '.join(sorted((output_numbers[x][y-1], output_numbers[x+1][y]))))
elif output_numbers[x][y] == output_numbers[-1][0]:
    print(' '.join(sorted((output_numbers[x][y+1], output_numbers[x-1][y]))))
elif output_numbers[x][y] == output_numbers[-1][-1]:
    print(' '.join(sorted((output_numbers[x][y-1], output_numbers[x-1][y]))))
# elif output_numbers[x][y] == output_numbers[0][y]:
#     print(' '.join(sorted((output_numbers[x][y-1], output_numbers[x][y+1],
#           output_numbers[x+1][y]))))
# elif output_numbers[x][y] == output_numbers[0][y] and n == 1:
    # print(' '.join(sorted((output_numbers[x][y-1], output_numbers[x][y+1]))))
elif output_numbers[x][y] == output_numbers[-1][y]:
    print(' '.join(sorted((output_numbers[x][y-1], output_numbers[x][y+1],
          output_numbers[x-1][y]))))
elif output_numbers[x][y] == output_numbers[x][0]:
    print(' '.join(sorted((output_numbers[x][y+1], output_numbers[x-1][y],
          output_numbers[x+1][y]))))
elif output_numbers[x][y] == output_numbers[x][-1]:
    print(' '.join(sorted((output_numbers[x][y-1], output_numbers[x-1][y],
          output_numbers[x+1][y]))))
else:
    print(' '.join(sorted((output_numbers[x][y-1], output_numbers[x][y+1],
          output_numbers[x-1][y], output_numbers[x+1][y]))))
