def arithmetic_ops():
    print(f'2 + 2 = {2 + 2}')
    print(f'8 / 5 = {8 / 5} \t# a float')
    print(f'8 // 5 = {8 // 5} \t\t# floor division')
    print(f'17 % 3 = {17 % 3} \t\t# remainder')
    print(f'5 ** 2 = {5 ** 2} \t# power of')


def relational_ops():
    """
    Same level of precedence
    Evaluated from L->R
    """
    ...


def boolean_ops():
    """
    Order of precedence: not -> and -> or
    short-circult evaluation
    """
    ...


if __name__ == '__main__':
    arithmetic_ops()
