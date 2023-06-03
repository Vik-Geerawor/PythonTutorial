import os
from functools import partial


def power_of(n):
    """
    returns a function which:
    1. accepts an arg x, and
    2. returns a value raised to the power of n
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


def main():
    # power_of_two = power_of(2)
    # a = power_of_two(3)
    # print(a)

    lambda_delayed()


if __name__ == '__main__':
    os.system('clear')
    main()
