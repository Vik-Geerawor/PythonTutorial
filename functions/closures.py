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
        funcs.append(
            # NOTE: fixed through local variable in lambda
            lambda name=name: print(f"Hello {name}")
        )

    # Testing
    # for i in range(len(funcs)):
    #     funcs[i]()

    return funcs


def test_make_greetings():
    names = ['Vik', 'Brian', 'Jeniffer']
    greetings = make_greetings(names)
    for greeting in greetings:
        greeting()


def favourites_first():
    """
    Sorting a list of numbers in ascending order, however, putting 
    favourite numbers at the top of the list
    """
    numbers = [8, 3, 1, 2, 9, 5, 4, 7, 6]
    favourites = {7, 3, 8}

    numbers = sort_priority(numbers, favourites)

    print(numbers)


def sort_priority(numbers, favourites):
    """Closure function"""

    def helper(x):
        if x in favourites:
            found_favs = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return numbers


def main():
    # test_outer_func()
    # test_make_greetings()
    favourites_first()


if __name__ == '__main__':
    os.system('clear')
    main()
