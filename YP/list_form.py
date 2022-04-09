def list_form(x, k):
    """
    Для неотрицательного целого числа X
    списочная форма – это массив его цифр слева направо.
    Выведите списочную форму числа X+K.
    """
    xk = x + k
    return ' '.join(str(xk))


if __name__ == '__main__':
    len_list_form_x = int(input())
    x = int(''.join(input().split()))
    k = int(input())
    xk = list_form(x, k)
    print(xk)
