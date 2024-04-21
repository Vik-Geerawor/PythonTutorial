from os import system
from functools import reduce


def reduce_v1(nums):
    r = nums[0]
    for i in range(1, len(nums)):
        r *= nums[i]
    return r


def reduce_v2(nums):
    """
    the args of the func passed starts with the first 2 values from the list
    thereafter the result of the func is passed as one of the arg
    and the 2nd arg is the next item in the list
    returns a value thus reducing the list
    """
    r = reduce(lambda a, b: a * b, nums)
    return r


if __name__ == '__main__':
    system('clear')

    nums = [1, 2, 3, 4, 5]
    # 1 * 2 = 2
    # 2 * 3 = 6
    # 6 * 4 = 24
    # 24 * 5 = 120

    r = reduce_v1(nums)
    print(f"{r}")

    r = reduce_v2(nums)
    print(f"{r}")


# https://www.youtube.com/watch?v=cKlnR-CB3tk
