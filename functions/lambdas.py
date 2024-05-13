from os import system
from functools import partial


def power_of(n):
    """
    accepts an arg n which is an exponent
    returns a function which:
    1. accepts an arg x, and
    2. returns a value of x to the power of n
    """
    return lambda x: x ** n


def lambda_delayed():
    """
    returns a func which takes 2 numbers and returns their sum
    """
    def add(a, b):
        return a + b

    a = 2
    b = 3
    def f(): return add(a, b)
    g = partial(add, a, b)

    a = 20
    b = 30

    x = f()
    y = g()
    print(f"lambda: x = {x}")
    print(f"partial: y = {y}")


if __name__ == '__main__':
    system('clear')

    power_of_two = power_of(2)
    a = power_of_two(3)
    print(a)
    lambda_delayed()
