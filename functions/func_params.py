import os


def standard_params(a: int, b: int) -> None:
    print(f"a={a} b={b}")


def positional_params(a: int, b: int, /) -> None:
    print(f"a={a} b={b}")


def args_params(*x: int) -> None:
    print(f"x={x}")


def kwargs_params(**x: int) -> None:
    print(f"x={x}")


if __name__ == "__main__":
    os.system('clear')

    # standard_params(1, 2)
    # standard_params(b=1, a=2)

    # positional_params(1, 2)
    # positional_params(b=1, a=2)   # ERROR: positional-only

    # args_params(1, 2)
    # args_params(1, 2, 3)

    x = {'a': 1, 'b': 2, 'c': 3}
    kwargs_params(**x)
