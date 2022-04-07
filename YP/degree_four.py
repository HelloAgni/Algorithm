import math
import sys

sys.path.insert(0, "../my_decorators")
from timer_dec import main_timer


@main_timer
def degree_four(n):
    """
    Выведите «True», если число является степенью четырёх,
    «False» –— в обратном случае.
    """
    z = math.log(n, 4)
    if int(z) == z:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    n = int(input())
    degree_four(n)
