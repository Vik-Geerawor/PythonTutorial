import os
import time


def outer_func():
    """
    inner func needs to be called multiple update the same variable
    critical parts:
    1. the variable/s maintaining the state
    2. the inner function - closure func
    3. both need to be bundled together
    """
    list1 = []

    # NOTE: Call-back function
    def inner_func(x):
        list1.append(x)
        print(list1)

    return inner_func


def make_greetings(names):
    """
    Internal python design of variable sharing leads to unexpected results
    When each of the functions from the list is actually called
    the variable `name` only has 1 value
    and that is 'Jeniffer'
    Lesson: Never even used a non-local or global var
    """
    funcs = []

    for name in names:
        funcs.append(lambda: print(f"Hello {name}"))
        # funcs.append(lambda name=name: print(f"Hello {name}"))    # NOTE: Fix

    # Testing
    # for i in range(len(funcs)):
    #     funcs[i]()

    return funcs


def main():
    os.system('clear')

    # add_num = outer_func()
    # add_num(1)
    # add_num(2)
    # add_num(3)

    a, b, c = make_greetings(['Vik', 'Brian', 'Jeniffer'])
    a()
    b()
    c()


main()
