def list_comprehension():
    # old way
    # even_numbers = []
    # for x in range(10):
    #     if x % 2 == 0:
    #         even_numbers.append(x)

    # new ways
    # [<expr> <for clause> [1 or more for and/of if clauses]]
    new_even_nums = [x for x in range(10) if x % 2 == 0]
    # return x, for x in range, if x is even

    print(f'Listcomp - even nums: {new_even_nums}')

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    transposed = [[row[i] for row in matrix] for i in range(4)]
    print(f"Netsted listcomp: {transposed}")

    transposed = list(zip(*matrix))
    print(f"Zip: {transposed}")


def set_comprehension():
    lst = [1, 2, 2, 3, 4, 7, 4, 5, 8, 9, 3]
    s = {x for x in lst}
    print(s)


def dict_comprehension():
    times_2_table = {x: x * 2 for x in range(10)}
    print(f"Times 2 table: {times_2_table}")


def generators():
    """
    @returns:   a generator object
                generates values on demand
    """
    lst = [1, 2, 3, 4, 5]
    sq = (x**2 for x in lst)

    # NOTE: generate one value at a time
    print(next(sq))
    print(next(sq))
    print(next(sq))

    # NOTE: generate the rest of the values one at a time
    for i in sq:
        print(i)


if __name__ == '__main__':
    # list_comprehension()
    # set_comprehension()
    # dict_comprehension()
    generators()
