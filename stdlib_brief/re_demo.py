import re


def re_demo():
    """
    regex tools for advanced string processing
    """
    s = "The re module provides regular expression tools for advanced string processing"
    r = re.findall(r'\br.', s)
    print(r)

    s = "cat in the the hat hat hat"
    r = re.sub(r'(\b[a-z]+) \1', r'\1', s)
    print(r)
