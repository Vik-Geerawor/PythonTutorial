from os import system


def list_comp(lst):
    """
    @param: a list of numbers
    @return: a list of numbers
    Each number is the input list is raised to the power of 2 and added to
    the return list
    """
    return [x**2 for x in lst]    # list comp


def generator_expr(lst):
    """
    @param: a list of numbers
    @return: a generator object
    When used in a for loop, each loop raised the number to the power of 2
    and returns that value
    """
    return (x**2 for x in lst)


if __name__ == '__main__':
    system('clear')

    lst = [1, 2, 3, 4, 5]

    a = list_comp(lst)
    print(f"list comp return type: {type(a)}")
    for i in a:
        print(i, end=', ')
    print()

    b = generator_expr(lst)
    print(f"generator exp type: {type(b)}")
    for i in b:
        print(i, end=', ')
    print()
