import functools
import time


def timer(function_to_decorate):
    """Время выполнения декорируемой функции"""
    @functools.wraps(function_to_decorate)
    def wrapper_time(*args, **kwargs):
        start_time = time.time()
        value = function_to_decorate(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(
            f'Функция {function_to_decorate.__name__}'
            f' выполнена за {run_time:.7f} c.'
        )
        return value
    return wrapper_time


def check_number(value=None):
    """Декоратор проверки наличия числа в кортеже(списке)"""
    def check_func(function_to_decorate):
        @functools.wraps(function_to_decorate)
        def check_in(args):
            print('старт')
            if value in args:
                print('Условие выполнено')
                return function_to_decorate(args)
            else:
                print('Не выполнено')
                return function_to_decorate(args)
        return check_in
    return check_func


@timer
@check_number(value=5)
def check_numbers(num):
    print(f'Текущая функция: {check_numbers.__name__} params: {num}')


def exponentiation(value=None):
    """Декоратор возведения в степень value"""
    def func_decorator(func):
        @functools.wraps(func)
        def wrapper(args):
            x = f'Число {func(args)} в степени {value}'
            expo = args ** value
            print(f'{x} = {expo}')
            return x, expo
        return wrapper
    return func_decorator


@timer
@exponentiation(value=3)
def s_low(s):
    print(f'Число переданное в функцию: {s}')
    return s


def case_swapping(func):
    """Декоратор конвертирует регистр букв"""
    @functools.wraps(func)
    def wrapper(args):
        new_string = ''.join(list(map(
            lambda x: x.upper() if x == x.lower() else x.lower(), args)))
        print(new_string)
        return new_string
    return wrapper


@case_swapping
def zero_string(string):
    pass


# Params
num = (1, 2, 3, 5)
s = 3
string = 'HelloWorld'  # 'hELLOwORLD'

if __name__ == '__main__':
    check_numbers(num)
    s_low(s)
    zero_string(string)
