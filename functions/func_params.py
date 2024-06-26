import os


def standard_params(a: int, b: int) -> None:
    """
    Args can be passed as positional or keyword
    """
    print(f"a={a} b={b}")


def positional_only(a: int, b: int, /) -> None:
    """
    Args can only be passed as positional
    """
    print(f"a={a} b={b}")


def keyword_only(*, a: int = None, b: int) -> None:
    """
    Args can only be passed as keywords
    """
    print(f"{a=} {b=}")


# Variable Length Arguments

def args_params(*x: int) -> None:
    """
    Arg can contain more than one value
    """
    print(f"{type(x)=} {x=}")


def kwargs_params(**x: int) -> None:
    """
    Arg can contain more than one 'key: value' pair
    """
    print(f"{type(x)=} {x=}")


def combined_example(pos_only, /, pos_or_kw, *, kw_only, **kwargs):
    """
    pos-only before /
    keyword-only after * - N.B. *args cannot be used in this case
    """
    print(f"{pos_only=}, {pos_or_kw=}, {kw_only=}, {kwargs=}")


if __name__ == "__main__":
    os.system('clear')

    # standard_params(1, 2)
    # standard_params(b=1, a=2)

    # positional_only(1, 2)
    # # positional_only(b=1, a=2)   # ERROR: positional-only - true -ve

    # # keyword_only(1, 4)          # ERROR: keyword-only - true -ve
    # keyword_only(a=1, b=2)

    # args = [3, 4]
    # combined_example(1, 2, kwd_only=3)

    # a = [1, 2, 3]
    # args_params(*a)

    b = {'a': 1, 'b': 2, 'c': 3}
    # kwargs_params(**b)

    combined_example(1, 2, kw_only=3, **b)
