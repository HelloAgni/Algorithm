def simple_decorator(function_to_decorate):
    def simple_decorator_in(*args, **kwargs):
        print('выполню до вызываемой функции')
        print(args, len(args), (tuple(map(str, args))))
        print(dict(kwargs.items()))
        function_to_decorate(*args, **kwargs)
        print('выполню после вызываемой функции')
    return simple_decorator_in


@simple_decorator
def just_func(*args, **kwargs):  # <=> just_func = simple_decorator(just_func)
    print('just_func - ничего особенного')


li = [1, 2, 3, 4]
d = {'a': 1, 'b': 2, 'c': 3}
z = {'r': 1, 'br': 2, 'cr': 3, **d}
just_func(*li, **z)

# just_func = simple_decorator(just_func)
# just_func()
