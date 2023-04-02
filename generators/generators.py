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


class GeneratorClass:
    def __init__(self, max) -> None:
        self.max = max

    def __iter__(self):
        """
        This is a generator function, coz it contains yield
        """
        i = 1
        while i <= self.max:     # NOTE: only the while loop is iterated over
            yield i
            i += 1


def demo_generator_func(max):
    increment = generator_func(max)

    for num in increment:
        print(num, end=', ')
    print()

    print(f"Re-iterating")          # NOTE: Does not work if it's a func
    for num in increment:
        print(num, end=', ')
    print()


def demo_generator_class(max):

    counter = GeneratorClass(max)

    for num in counter:
        print(num, end=', ')
    print()

    print(f"Re-iterating")
    for num in counter:                   # NOTE: That's how to do it twice, using class
        print(num, end=', ')
    print()


def combining_generators(max):
    """
    Combines to generators into one
    @param: max value
    """
    yield from generator_func(max)      # NOTE: first generator
    yield from range(10, 50, 5)


if __name__ == '__main__':
    system('clear')

    max = 10

    # print(f"Calling demo_yield_func")
    # demo_yield_func(max)

    # print(f"Calling demo_yield_class")
    # demo_yield_class(max)

    print(f"Calling combining_generators")
    for x in combining_generators(max):
        print(x, end=', ')
    print()
