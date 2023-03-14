"""
As guidance:

Use positional-only if you want:

1. the parameter name not to be available to the users
2. to enforce the order of the arguments when the function is called
3. to take some positional parameters and arbitrary keywords

Use keyword-only
1. when names have meaning and the function definition is more 
understandable by being explicit with names
2. to prevent users relying on the position of the argument being passed

For an API, use positional-only to prevent breaking API changes if the 
parameter’s name is modified in the future.
"""


def fib(n):
    """
    Print a Fibonacci series up to n    # NOTE: docstring
    """
    result = []
    a, b = 0, 1
    while a < n:
        # print(f'{a}', end=' ')
        result.append(a)
        a, b = b, a + b
    # print()
    return result


def f_default_arg(a, b=1):              # NOTE: Polymorphism
    """
    Function with
    - 1 mandatory positional param - a
    - 1 optional positional param - b, with a default value of 1
    """
    return a * b


def standard_arg(arg):
    """
    Mandatory NON-POS param
    """
    print(arg)


def pos_only_arg(arg, /):
    """
    Mandatory POS param
    """
    print(arg)


def kwd_only_arg(*, arg):
    """
    Mandatory positional param
    """
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    """
    Mandatory positional param
    """
    print(pos_only, standard, kwd_only)


def arb_no_of_args(a, *args):
    """
    a - is a mandatory positional param
    *args - is an optional tuple of args
    """
    print(f'positional arg = {a}')

    if args:
        print(f'*arg is a tuple of args = {args}')


def arb_no_of_kwargs(a, **kwargs):
    """
    a - is a mandatory positional param
    *kwargs - is an optional dict of keyword args
    """
    print(f'position arg = {a}')

    if kwargs:
        print(f'kwargs is a dict of keyword args = {kwargs}')


def power_of(n):
    """
    n - is the exponent and is fixed at the point of the function call
    The function returns another function with the ability to calculate
    the power of the fixed value of n, e.g. 2 (power of 2)
    x - is the variable which is then passed to the above function to calc
    it's power of the fixed value of n, i.e. 3 to the power of 2

    """
    return lambda x: x ** n


def main():
    # result = fib(100)
    # print(result)

    # result = f_default_arg(5)
    # print(result)

    # result = f_default_arg(5, 2)
    # print(result)

    # standard_arg(2)
    # standard_arg(arg=2)

    # pos_only_arg(3)
    # pos_only_arg(arg=3)         # ERROR - only pos arg allowed

    # kwd_only_arg(4)             # ERROR - only kwd arg allowed
    # kwd_only_arg(arg=4)

    # combined_example(2, standard=3, kwd_only=4)

    # arb_no_of_args(3)
    # args = [10, 20, 30]
    # arb_no_of_args(2, *args)          # NOTE: *args <- list as arg

    # arb_no_of_kwargs(5)
    kwarg = {'tens': 10, 'twenty': 20, 'thirty': 30}
    arb_no_of_kwargs(5, **kwarg)        # NOTE: Amazing..! dictionary as arg

    # to_the_power_of_2 = power_of(2)   # NOTE: lambda func returned
    # x = to_the_power_of_2(3)
    # print(x)
