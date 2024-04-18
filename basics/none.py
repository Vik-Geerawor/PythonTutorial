from os import system


def my_none(obj):
    """
    The None object has a single value, representing the absence of value
    The name of the object is 'None'
    The truth value is 'false'
    """
    return type(obj)


if __name__ == "__main__":
    # clear screen
    system("clear")

    a: int
    print(f"{my_none(a)}")
