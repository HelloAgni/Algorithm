from re import sub


def to_camel_case(text):
    """
    Convert string to camel case
    "the-stealth-warrior" gets converted to "theStealthWarrior"
    "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
    """
    if text == '':
        print(text)
    elif text[0] == text[0].lower():
        text = sub(r"(_|-)+", " ", text).title().replace(" ", "")
        print(f'1ый - {text}')
        first_lower = ''.join([text[0].lower(), text[1:]])
        print(f'2ый - {first_lower}')
    else:
        text = sub(r"(_|-)+", " ", text).title().replace(" ", "")
        print(f'3ий - {text}')


# v2

def to_camel_case_v2(text):
    new_text = sub('[_-](.)', lambda x: x.group(1).upper(), text)
    print(new_text)


# text = 'the-stealth-warrior'
text = 'The_Stealth_Warrior'
# text = ''
to_camel_case(text)
to_camel_case_v2(text)
