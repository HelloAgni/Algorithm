def strip_comments(strng, markers):
    """
    Complete the solution so that it strips all text that follows
    any of a set of comment markers passed in.
    Any whitespace at the end of the line should also be stripped out.
    'apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
    => 'apples, pears\ngrapes\nbananas'
    """
    st = strng.split('\n')
    for marker in markers:
        st = [x.split(marker)[0].rstrip() for x in st]
    return '\n'.join(st)


strng = 'a #b\nc\nd $e f g'  # 'a\nc\nd'
markers = ['#', '$']
print(strip_comments(strng, markers))
