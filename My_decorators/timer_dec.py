import functools
import time


def main_timer(function_to_decorate):
    """
    @main_timer
        import sys
        sys.path.insert(0, "../My_decorators")
        from timer_dec import main_timer
    Время выполнения декорируемой функции
    """
    @functools.wraps(function_to_decorate)
    def wrapper_time(*args, **kwargs):
        start_time = time.time()
        function_to_decorate(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(
            f'Функция {function_to_decorate.__name__}'
            f' выполнена за {run_time:.7f} c.'
        )
        # return function_to_decorate(*args, **kwargs)
    return wrapper_time
