import functools
import time


def timer(function_to_decorate):
    """Время выполнения декорируемой функции"""
    @functools.wraps(function_to_decorate)
    def wrapper_time(*args, **kwargs):
        # print('выполню до вызываемой функции')
        start_time = time.time()
        value = function_to_decorate(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(
            f'Функция {function_to_decorate.__name__}'
            f' выполнена за {run_time:.5f} c.'
        )
        return value
        # print('выполню после вызываемой функции')
    return wrapper_time


@timer
def just_func(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(1000)])


def check(function_to_decorate):
    """Декоратор проверки условия"""
    @functools.wraps(function_to_decorate)
    def check_in(*args, **kwargs):
        print('старт')
        for _ in args:
            if _ >= 5:
                print('Условие выполнено')
                function_to_decorate(*args, **kwargs)
            else:
                print('Не выполнено')
                function_to_decorate(*args, **kwargs)
    return check_in


@timer
@check
def check_numbers(num):
    print(f'{num}')


if __name__ == '__main__':
    num = 5
    # just_func(10)
    check_numbers(num)
