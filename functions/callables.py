from os import system


def hello(name: str):
    """A simple function.

    Parameters
    ----------
    name : str
        A person's name.

    Returns
    -------
    None
        Doesn't return anything
    """
    print(f"Hello {name.title()}, how are ya!?")


if __name__ == '__main__':
    # clear screen
    system("clear")

    name = "vik"

    # NOTE: This is a callable function
    a = hello
    # print(f"{type(a)=}")

    # NOTE: Read-Only Attributes
    print(f"{type(a.__globals__)=}")
    print(f"{a.__globals__=}")

    # NOTE: Writeable Attributes
    # print(f"{type(a.__closure__)=}")
    # print(f"{a.__closure__=}")

    # print(f"{type(a.__qualname__)=}")
    # print(f"{a.__qualname__=}")

    # print(f"{type(a.__module__)=}")
    # print(f"{a.__module__=}")

    # print(f"{type(a.__name__)=}")
    # print(f"{a.__name__=}")

    # print(f"{type(a.__annotations__)=}")
    # print(f"{a.__annotations__=}")

    # print(f"{type(a.__closure__)=}")
    # print(f"{a.__closure__=}")
