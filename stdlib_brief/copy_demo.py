import os
from copy import deepcopy


def pointers(list1, list2):
    a = list1
    b = list2

    # NOTE: a dn b refer to the same memory location
    b = a

    print(f"\nb is a: {b is a}")
    print(f"ID: a = {id(a)}")
    print(f"ID: b = {id(b)}")


def shallow_copy(list1, list2):
    # NOTE: shallow copy
    b = list(a)
    print(f"\nb is a: {b is a}")
    print(f"ID: a = {id(a)}")
    print(f"ID: b = {id(b)}")

    b.append(6)
    print(f"a={a}")
    print(f"b={b} - after update")

    b[2][0] = 5
    print(f"\na={a} - checkout a")     # NOTE: a is modified
    print(f"b={b} - after update")


def deep_copy(list1, list2):
    a = list1
    b = list2

    b = deepcopy(a)
    print(f"\nb is a: {b is a}")
    print(f"ID: a = {id(a)}")
    print(f"ID: b = {id(b)}")

    b.append(6)
    print(f"a={a}")
    print(f"b={b} - after update")

    b[2][0] = 5
    print(f"\na={a}")     # NOTE: a is modified
    print(f"b={b} - after update")


if __name__ == "__main__":
    os.system('clear')

    a = [1, 2, [3, 4]]
    b = None

    # pointers(a, b)
    # shallow_copy(a, b)
    deep_copy(a, b)
