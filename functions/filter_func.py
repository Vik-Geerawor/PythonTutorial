from os import system

"""
applying a filter to a list based on a condition
"""


def over_two(nums):
    filtered_nums = [x for x in nums if x > 2]
    return filtered_nums


def over_two_v2(nums):
    """
    filter applies the func passed to each item in the list
    and returns a filter object
    which is iterable
    """
    filtered_nums = filter(lambda x: x > 2, nums)
    return filtered_nums


def main():
    system('clear')

    nums = [1, 2, 3, 4, 5]
    n1 = over_two(nums)
    print(f"type n1 {type(n1)}")
    for x in n1:
        print(f"{x}", end=', ')
    print()

    n2 = over_two_v2(nums)
    print(f"type n2: {type(n2)}")
    for x in n2:
        print(f"{x}", end=', ')
    print()


main()
