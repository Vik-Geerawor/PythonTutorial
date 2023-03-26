def power_of(n):
    """
    n - is the exponent and is fixed at the point of the function call
    The function returns another function with the ability to calculate
    the power of the fixed value of n, e.g. 2 (power of 2)
    x - is the variable which is then passed to the above function to calc
    it's power of the fixed value of n, i.e. 3 to the power of 2

    """
    return lambda x: x ** n