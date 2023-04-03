from os import system


def generator_func(max):
    """
    This is a generator function. Calling it returns a generator object
    To get the values, the __next__() method needs to be invoked by other code
    e.g. a for loop
    @param: maximum value to be generated
    @return: a generator object
    """
    i = 1
    try:                    # NOTE: ensures clean GC
        while i <= max:     # NOTE: only the while loop is iterated over
            yield i
            i += 1
    finally:
        print(f"Exiting yield_func")
    # return None           # NOTE: we don't return anything


def combining_generators(max):
    """
    Combines to generators into one
    @param: max value
    """
    print(f"\nStarting first generator")
    yield from generator_func(max)      # NOTE: first generator

    print(f"\nStarting second generator")
    yield from range(10, 50, 5)


if __name__ == '__main__':
    system('clear')

    max = 10

    print(f"Calling combining_generators")
    for x in combining_generators(max):
        print(x, end=', ')
    print()
