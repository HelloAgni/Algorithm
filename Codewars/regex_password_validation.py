import re


def check(password):
    """
    regex => '4fdg5Fj3' => True
    regex => 'DHSJdhjsU'=> False
    regex => 'fjd3IR9.;' => False

    ^              # begin word
    (?=.*?[a-z])   # at least one lowercase letter
    (?=.*?[A-Z])   # at least one uppercase letter
    (?=.*?[0-9])   # at least one number
    [A-Za-z0-9]    # only alphanumeric
    {6,}           # at least 6 characters long
    $              # end word
    """
    # works same
    # if re.fullmatch(
    #         r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])[A-Za-z0-9]{6,}$', password):
    #     return True
    if re.fullmatch(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$', password):
        return True
    else:
        return False


ps = {
    'Password123': True,
    'fjd3IR9': True,
    'ghdfj32': False,
    'DSJKHD23': False,
    'dsF43': False,
    '4fdg5Fj3': True,
    'DHSJdhjsU': False,
    'fjd3IR9.;': False,
    'djI38D55': True
    }
for x in ps:
    print(check(x))
