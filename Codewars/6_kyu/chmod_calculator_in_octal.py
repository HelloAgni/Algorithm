"""
Chmod provides two types of syntax that can be used for changing permissions.
An absolute form using octal to denote which permissions bits are set e.g: 766.
Your goal in this kata is to define the octal
you need to use in order to set yout permission correctly.

Here is the list of the permission you can set with the octal
representation of this one.

    User
        read (4)
        write (2)
        execute (1)
    ...
"""
PERMISSION = {
    'r': 4,
    'w': 2,
    'x': 1
}


def chmod_calculator(perm):
    result = {'user': 0, 'group': 0, 'other': 0}
    for item in perm:
        elements_sum = 0
        for elements in perm.get(item):
            if elements == '-':
                elements_sum += 0
            else:
                elements_sum += PERMISSION.get(elements)
        result[item] = elements_sum
    return ''.join([str(x) for x in result.values()])


assert chmod_calculator(
    {"user": 'rwx', "group": 'r-x', "other": 'r-x'}) == "755", (
    'Ouput must be 755')
assert chmod_calculator(
    {"user": 'rwx', "group": 'r--', "other": 'r--'}) == "744", (
    'Ouput must be 744')
assert chmod_calculator(
    {"user": 'r-x', "group": 'r-x', "other": '---'}) == "550", (
    'Ouput must be 550')
assert chmod_calculator({"group": 'rwx'}) == "070", 'Output must be 070'
assert chmod_calculator({}) == "000", 'Output must be 000'

chm = {"user": 'rwx', "group": 'r-x', "other": 'r-x'}
print(chmod_calculator(chm))
