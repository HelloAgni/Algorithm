import functools


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


def case_swapping(func):
    """Декоратор конвертирует регистр букв"""
    @functools.wraps(func)
    def wrapper(args):
        func(args)
        new_string = ''.join(list(map(
            lambda x: x.upper() if x == x.lower() else x.lower(), args)))
        print(new_string)
        return new_string
    return wrapper


@exponentiation(value=3)
def s_low(number):
    pass


@case_swapping
def zero_string(string):
    pass
