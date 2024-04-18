from os import system


def strings():
    """
    Usage: Demonstrates how strings are declared and used
    This is a doc string, so it can be used for documentation
    :return: None
    """
    message = "Hello"
    print(message + "world")

    name = "Vik"
    print(message + name)

    print(f"strings are lists - name[0] = {name[0]}")


def str_to_unicode(in_str: str):
    """
    Returns a list of unicode values for each character
    in the input string.
    """
    str_code = []
    for char in in_str:
        str_code.append(ord(char))

    return str_code


def unicode_to_string(code: int) -> str:
    """
    Returns the character for the unicode in 
    decimal format.
    """
    return chr(code)


def str_to_bytes(my_str: str):
    """Converts a string to bytes.

    Parameters
    ----------
    my_str : str
        Input string

    Returns
    -------
    int
        A series of bits.
    """
    return str.encode(my_str)


def bytes_to_str(str_bytes):
    """Converts a byte string to a character string.

    Parameters
    ----------
    str_bytes : byte.
        A string in bytes.

    Returns
    -------
    str
        A string
    """
    pass


if __name__ == "__main__":
    # clear screen
    system("clear")

    strings()

    name = "vik geerawor"
    name_code = str_to_unicode(name)
    print(f"Name: {name}")
    print(f"Name in code: {name_code}")

    new_name = ''.join(unicode_to_string(code) for code in name_code)
    print(f"{new_name}")

    f_name_in_bytes = str_to_bytes("vik")
    print(f"{f_name_in_bytes}")
