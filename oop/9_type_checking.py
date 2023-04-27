from os import system

"""
1. A class is a type
2. An object of a subclass is of type of any of it's parent
"""


class A:
    pass


class B(A):
    pass


class C(B):
    pass


def class_type_check():
    # NOTE: check for class type of an object
    c = C()
    print(f"c is of type A: {isinstance(c, A)}")
    print(f"c is of type B: {isinstance(c, B)}")
    print(f"c is of type C: {isinstance(c, C)}")

    # NOTE: check of inheritance
    print(f"B is subclass of A {issubclass(B, A)}")
    print(f"C is subclass of B {issubclass(C, B)}")
    print(f"C is subclass of A {issubclass(C, A)}")


if __name__ == '__main__':
    system('clear')

    class_type_check()
