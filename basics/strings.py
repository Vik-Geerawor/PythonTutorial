def strings():
    """
    Usage: Demonstrates how strings are declared and used
    This is a doc string, so it can be used for documentation
    :return: None
    """
    message = 'Hello'
    print(message + 'world')

    name = "Vik"
    print(message + name)

    print(f'strings are arrays - name[0] = {name[0]}')


def main():
    strings()
