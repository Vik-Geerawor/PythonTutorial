import operator


def arithmetic_ops():
    print(f"2 + 2 = {2 + 2}")
    print(f"5 - 2 = {5 - 2}")
    print(f"2 * 3 = {2 * 3}")
    print(f"8 / 5 = {8 / 5} \t# a float")
    print(f"8 // 5 = {8 // 5} \t# floor division")
    print(f"17 % 3 = {17 % 3} \t# remainder")
    print(f"5 ** 2 = {5 ** 2} \t# power of")


def relational_ops():
    """
    Same level of precedence
    Evaluated from L->R
    """
    x = 2
    y = 3
    if x < y:
        print(f"{x} < {y}")


def matmul_demo():
    """
    Not implemented by any built-in types
    """
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    r = a @ b
    print(r)


def boolean_ops():
    """
    Order of precedence: not -> and -> or
    short-circult evaluation
    """
    ...


if __name__ == "__main__":
    # arithmetic_ops()
    matmul_demo()
