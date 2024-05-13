from os import system
import sys
import gc


if __name__ == "__main__":
    system('clear')

    # NOTE: everything is an object
    a = 1
    print(f"{id(a)=}, {type(a)=}, {a=}")

    a = a + 2
    a = a.__add__(3)    # NOTE: ops are are methods
    print(f"{a=}")

    if isinstance(a, list):
        print(f"a is a list")
    elif isinstance(a, int):
        print(f"a is an int")

    b = a
    c = b
    print(f"Pointers: {sys.getrefcount(a)}")

    # NOTE: invoke GC
    gc.collect()
