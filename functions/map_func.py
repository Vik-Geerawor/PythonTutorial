from os import system


def square(nums):
    squared_nums = []
    for x in nums:
        squared_nums.append(x * x)

    return squared_nums


def square_v2(nums):
    """
    map applies the func passed to each item in the list
    and returns a map object
    which is iterable
    """
    return map(lambda x: x * x, nums)


def square_v2(nums):
    return [x * x for x in nums]        # NOTE: List comp


def main():
    system('clear')

    nums = [1, 2, 3, 4, 5]

    s1 = square(nums)
    print(f"type s1: {type(s1)}")
    for x in s1:
        print(f"{x}", end=', ')
    print()

    s2 = square_v2(nums)
    print(f"type s2: {type(s2)}")
    for x in s2:
        print(f"{x}", end=', ')
    print()


main()
