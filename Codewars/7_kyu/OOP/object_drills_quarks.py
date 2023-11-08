class Quark():
    """
    Your Quark class should allow you to create quarks of any valid color
    ("red", "blue", and "green") and any valid flavor
    ('up', 'down', 'strange', 'charm', 'top', and 'bottom').
    Every quark has the same baryon_number: 1/3.
    Every quark should have an .interact()method that allows any quark
    to interact with another quark via the strong force.
    When two quarks interact they exchange colors.
    >>> q1 = Quark("red", "up")
    >>> q1.color
    "red"
    >>> q1.flavor
    "up"
    >>> q2 = Quark("blue", "strange")
    >>> q2.color
    "blue"
    >>> q2.baryon_number
    0.3333333333333333
    >>> q1.interact(q2)
    >>> q1.color
    "blue"
    >>> q2.color
    "red"
    """
    baryon_number = 1 / 3

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def interact(self, other):
        self.color, other.color = other.color, self.color


q1 = Quark('red', 'up')
q2 = Quark("blue", "strange")
print(q1.baryon_number)
print(q1.color)
print(q2.color)
q1.interact(q2)

print('Change q1', q1.color)
print('Change q2', q2.color)
