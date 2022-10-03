import re


def is_a_valid_message(msg):
    """
    For example "3hey5hello2hi" should be split into 3, hey, 5, hello, 2,
    hi and the function should return true, because "hey" is 3 characters,
    "hello" is 5, and "hi" is 2; as the numbers and the character counts match,
    the result is true.
    """
    if msg == '':
        return True
    if not msg[0].isdigit():
        return False
    x = re.findall(r'(\d+)([a-zA-Z]+|$)', msg)
    for _ in x:
        if int(_[0]) != len(_[-1]):
            return False
    return True


message = '4code13hellocodewars'
print(is_a_valid_message(message))
