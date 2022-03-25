from my_decorators import simple_decorator


@simple_decorator.timer
def swap(string_):
    """
    Given a string, swap the case for each of the letters.
    e.g. CodEwArs --> cODeWaRS
    Examples:
    ""           ->   ""
    "CodeWars"   ->   "cODEwARS"
    "abc"        ->   "ABC"
    "ABC"        ->   "abc"
    "123235"     ->   "123235"
    """
    new_string = list(
        map(lambda x: x.upper() if x == x.lower() else x.lower(), string_)
    )
    print(''.join(new_string))

# v2


@simple_decorator.timer
def swap_v2(string_):
    print(string_.swapcase())

# v3_decorator


@simple_decorator.timer
@simple_decorator.case_swapping
def swap_v3(string_):
    print(string_)


string_ = 'HelloWorld'
swap(string_)
swap_v2(string_)
swap_v3(string_)
