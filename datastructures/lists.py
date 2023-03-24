def list_demo():
    """
    Usage: contains mutable homogeneous sequence of elements as a list

    """

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

    print(
        f"Popped out {favourites.pop(favourites.index('apple'))}: {favourites}")


if __name__ == '__main__':
    # list_demo()
