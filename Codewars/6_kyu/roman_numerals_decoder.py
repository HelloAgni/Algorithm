SYMBOLS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
SYMBOLS_ = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}


def solution(s):
    """
    Create a function that takes a Roman numeral as its argument and
    returns its value as a numeric decimal integer
    """
    year = 0
    for num in SYMBOLS_.keys():
        if num in s:
            year += SYMBOLS_[num]
            s = s.replace(num, '')
    for num in s:
        year += SYMBOLS[num]
    return year


a = 'XXI'  # 21
b = 'MCMXC'  # 1990
c = 'MMVIII'  # 2008
d = 'MDCLXVI'  # 1666
print(solution(a))
print(solution(b))
print(solution(c))
print(solution(d))
