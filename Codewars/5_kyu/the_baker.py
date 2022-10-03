def cakes(recipe, available):
    """
    Write a function cakes(), which takes the recipe (object) and
    the available ingredients (also an object) and
    returns the maximum number of cakes (integer).
    # must return 2
    cakes({flour: 500, sugar: 200, eggs: 1},
    {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
    # must return 0
    cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100},
    {sugar: 500, flour: 2000, milk: 2000})
    """
    new = []
    for x in recipe:
        if x in available:
            new.append(available[x] // recipe[x])
        else:
            return 0
    return min(new)


def cakes_v2(recipe, available):
    return min([available[x] // recipe[x] if x in available else 0 for x in recipe])


rec = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
av = {"sugar": 500, "flour": 2000, "milk": 2000}
rec_2 = {"flour": 500, "sugar": 200, "eggs": 1}
av_2 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes_v2(rec_2, av_2))
print(cakes_v2(rec, av))
