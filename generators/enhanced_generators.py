from contextlib import contextmanager
from os import system


def echo():
    try:
        while True:
            n = yield
            print(f"{n} {n} {n}...")
    except GeneratorExit as e:
        print(f"Generator closed: {e}")


def demo_echo():
    e = echo()
    e.send(None)            # NOTE: first send is always None
    e.send('hello')
    e.send('world')
    e.close()               # NOTE: to close the generator obj


@contextmanager
def ctx_manager():
    print("Entering")
    i = 1
    try:
        while i < 10:
            yield i
            i += 1
    except Exception as e:
        print("An error occurred", e)
    finally:
        print("Leaving")


def demo_ctx_manager():
    print(type(ctx_manager()))
    with ctx_manager() as val:
        print(val)


class EnhancedYieldClass:
    def __init__(self) -> None:
        pass

    def __enter__(self):
        print(f"Entering EYC context")

    @contextmanager
    def manager(self, max):
        i = 2
        try:
            while i < max:
                yield i
                i += 1
        finally:
            pass

    def __exit__(self, ty, val, tb):
        print(f"Exiting EYC context")


def demo_EnhancedYieldClass():

    context = EnhancedYieldClass()

    with context.manager(10) as c:
        for i in c:
            print(i, end=', ')
        print()


if __name__ == '__main__':
    system('clear')
    # demo_echo()
    demo_ctx_manager()
    # demo_EnhancedYieldClass()
