from os import system
from functools import reduce


def reduce_v1(nums):
    r = nums[0]
    for i in range(1, len(nums)):
        r *= nums[i]
    return r


def reduce_v2(nums):
    r = reduce(lambda a, b: a * b, nums)
    return r


def main():
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


main()


# https://www.youtube.com/watch?v=cKlnR-CB3tk
