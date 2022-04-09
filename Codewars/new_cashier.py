def get_order(order):
    """
    All the orders they create look something like this:
    "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
    Their preference is to get the orders as a nice clean string
    with spaces and capitals like so:
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
    return new_order[:-1]


order = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
get_order(order)
