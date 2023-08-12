import doctest


def average(values):
    """
    doctest uses the docstring to validate a function.
    The 2 lines are used to do so. doctest executes the function with
    the args as given below and check that the result matches.
    >>> print(average([20, 30, 70]))
    40.0
    """

    return sum(values) / len(values)


r = doctest.testmod()       # automatically validates the enbedded test
print(r)


# Ref: https://docs.python.org/3/tutorial/stdlib.html#quality-control
