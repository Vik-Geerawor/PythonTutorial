from datetime import datetime
import functools
# from ..utilities.perfmon import timer
# NOTE: python -m decorators.decorators
from utilities.perfmon import timer


def decorator(func):
    """
    decorator boilerplate
    """
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # NOTE: do something before
        value = func(*args, **kwargs)
        # NOTE: do something after
        return value
    return wrapper_decorator


def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print(f"*** Pre func call ***")
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
        print(f"*** Post func call ***")
    return wrapper


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)               # NOTE: accepts args
        return func(*args, **kwargs)        # NOTE: and returns value
    return wrapper_do_twice


@my_decorator
def say_whee():
    print(f"Whee!")


@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice
def return_greeting(name):
    print(f"Creating greeting")
    return f"Hi {name}"


if __name__ == "__main__":
    # f = my_decorator(say_whee)
    # f()
    # say_whee()

    # greet("Vik")

    # r = return_greeting("Vik")
    # print(r)

    @timer
    def waste_some_time(num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(10000)])

    r = waste_some_time(100)
    print(r)
