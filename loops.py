
def for_loop():
    shopping_list = ['banana', 'apple', 'coconut', 'mango', 'strawberry']

    for items in shopping_list:
        print(items)

    for i in range(10, 20, 2):
        print(i, end='-')

    for i in range(len(shopping_list)):
        print(f'{i}. {shopping_list[i]}')

    for rank, item in enumerate(shopping_list):
        print(f'{rank}-{item}')


def break_statement():
    for n in range(2, 100):
        for x in range(2, n):
            if n % x == 0:
                print(f'{n} / {x} = {n // x}')
                break                           # NOTE: break out of the inner loop
        else:                                   # NOTE: and executes the else block
            print(f'{n} is a prime number')


def continue_statement():
    for n in range(2, 10):
        if n % 2 == 0:
            print(f'{n} is even')
            continue                            # NOTE: continues to top of the loop
        print(f'{n} is odd')


def fibonacci_series():
    a, b = 0, 1
    while a < 10:
        print(a, end=',')
        a, b = b, a + b


def main():
    fibonacci_series()
    for_loop()
    break_statement()
    continue_statement()
