from my_decorators import simple_decorator


@simple_decorator.timer
def get_order(order):
    """
    "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
    """
    menu = ['burger',
            'fries',
            'chicken',
            'pizza',
            'sandwich',
            'onionrings',
            'milkshake',
            'coke']
    new_order = ''
    for i in menu:
        x = (i.capitalize() + ' ')
        y = order.count(i)
        new_order += x * y
    print(new_order[:-1])

# v2


order = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
get_order(order)
