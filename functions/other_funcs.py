from os import system


def generator_expr(nums):
    squares = (x * x for x in nums)
    print(f"Type: squares = {type(squares)}")
    for n in squares:
        print(n, end=', ')
    print()


def map_demo(nums):
    squares = map(lambda x: x * x, nums)
    print(f"Type: squares = {type(squares)}")
    for n in squares:
        print(n, end=', ')
    print()


def filter_demo(nums):
    for n in filter(lambda x: x > 2, nums):
        print(n, end=', ')
    print()


def main():
    system('clear')

    nums = [1, 2, 3, 4, 5]

    generator_expr(nums)
    map_demo(nums)
    filter_demo(nums)


main()
