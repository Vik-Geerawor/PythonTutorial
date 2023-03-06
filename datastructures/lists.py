def my_list():
    shopping_list = ['banana', 'apple', 'coconut', 'mango', 'strawberry']
    print(f"My orig list: {shopping_list}")

    # index
    print(f"First item: {shopping_list[0]}")
    print(f"Last item: {shopping_list[-1]}")

    # slicing
    favourites = shopping_list[0:3]
    print(f"My favourties: {favourites}")
    print(f"My favourties in reverse: {favourites[::-1]}")

    favourites.append('mango')
    print(f"Append mango: {favourites}")

    favourites.insert(2, 'strawbery')
    print(f"Insert strawbery at index 2: {favourites}")

    favourites.index('coconut')
    print(f"Index of coconut: {favourites}")

    idx_apple = favourites.index('apple')
    print(
        f"Popped out {favourites.pop(favourites.index('apple'))}: {favourites}")


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


def main():
    # my_list()
    list_comprehension()
