import os


def outer_func() -> object:
    """
    Inner func needs to be called multiple times to update the same variable.
    Critical parts:
    1. the variable/s maintaining the state
    2. the inner function - closure func
    3. both need to be bundled together
    """
    list1 = []

    # NOTE: aka Callback function
    def inner_func(x: int):
        list1.append(x)
        print(list1)

    return inner_func


def test_outer_func():
    add_num = outer_func()
    add_num(1)
    add_num(2)
    add_num(3)


def make_greetings(names):
    """
    Internal python design of variable sharing leads to unexpected results.
    When each of the functions from the list is actually called
    the variable `name` only has 1 value, 'Jeniffer'
    Lesson: Never ever use a non-local or global var
    """
    funcs = []

    for name in names:
        # funcs.append(lambda: print(f"Hello {name}"))
        funcs.append(lambda name=name: print(
            f"Hello {name}"))    # NOTE: the fix

    # Testing
    # for i in range(len(funcs)):
    #     funcs[i]()

    return funcs


def test_make_greetings():
    names = ['Vik', 'Brian', 'Jeniffer']
    a, b, c = make_greetings(names)
    a()
    b()
    c()


def main():
    test_outer_func()
    test_make_greetings()


if __name__ == '__main__':
    os.system('clear')
    main()
