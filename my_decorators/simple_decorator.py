import functools

# import sys
# sys.path.insert(0, "../My_decorators")
# from py import _decorator_


def exponentiation(value=None):
    """Декоратор возведения в степень value"""
    def func_decorator(func):
        @functools.wraps(func)
        def wrapper(args):
            x = f'Число {args} в степени {value}'
            expo = args ** value
            print(f'{x} = {expo}')
            # return x, expo
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
        # return new_string
    return wrapper


#  example
def example_decorator(function_to_decorate):
    """
    Шаблон декоратора с аргументами
    """
    def wrapper_original_function(*args, **kwargs):
        print(f'Аргументы исходной функции {args} {kwargs}')
        function_to_decorate(*args, **kwargs)
        print('Код после функции')
    return wrapper_original_function


@exponentiation(value=3)
def d_degree(number):
    pass


@case_swapping
def zero_string(string):
    pass


@example_decorator
def check(*a, **b):
    pass
    # print(a, b)


if __name__ == '__main__':
    #  Examples
    a = [1, 2, 3]
    b = {'a': 1, 'b': 2}
    check(*a, **b)
    number = 5
    d_degree(number)
    string = 'HelloworlD'
    zero_string(string)
