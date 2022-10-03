import re


def valid_isbn(isbn):
    """
    ISBN-10 identifiers are ten digits long.
    The first nine characters are digits 0-9.
    The last digit can be 0-9 or X, to indicate a value of 10.
    An ISBN-10 number is valid if the sum of the digits
    multiplied by their position modulo 11 equals zero.
    Examples
    1112223339   -->  true
    111222333    -->  false
    """
    isbn = re.findall(r'X|\d', isbn)
    if len(isbn) == 10 and isbn[0].isdigit():
        new = [(lambda x: x)(10)*c if x == 'X' else int(x)*c for c, x in enumerate(isbn, 1)]
        return sum(new) % 11 == 0
    return False


ar = '048665088X'  # True
print(valid_isbn(ar))
