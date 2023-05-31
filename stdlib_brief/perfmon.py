from timeit import Timer


def perfmon(func):
    def wrapper():
        return Timer(func).timeit()

    return wrapper


@perfmon
def trad_swap():
    a = 1
    b = 2
    t = a
    a = b
    b = t

    return (a, b)


@perfmon
def tuple_swap():
    a = 1
    b = 2
    a, b = b, a

    return (a, b)


def timer_demo():
    """
    Timing performance of swapping values between 2 variables
    using the traditional mechanism vs tuple unpacking
    """

    trad = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
    print(f"{trad:0.5f}")

    tuple_unpk = Timer('a, b = b, a', 'a=1; b=2').timeit()
    print(f"{tuple_unpk:0.5f}")


p = trad_swap()
print(f"{p:0.5f}")

p = tuple_swap()
print(f"{p:0.5f}")
