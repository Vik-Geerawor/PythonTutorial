
def for_loop():
    shopping_list = ["banana", "apple", "coconut", "mango", "strawberry"]

    for items in shopping_list:
        print(items)

    for i in range(10, 20, 2):
        print(i, end="-")

    for i in range(len(shopping_list)):
        print(f"{i}. {shopping_list[i]}")

    for rank, item in enumerate(shopping_list):
        print(f"{rank}-{item}")


def break_statement():
    for n in range(2, 100):
        for x in range(2, n):
            if n % x == 0:
                print(f"{n} / {x} = {n // x}")
                break                           # NOTE: break out of the inner loop
        else:                                   # NOTE: and executes the else block
            print(f"{n} is a prime number")


def continue_statement():
    for n in range(2, 10):
        if n % 2 == 0:
            print(f"{n} is even")
            continue                            # NOTE: continues to top of the loop
        print(f"{n} is odd")


def while_loop():
    a, b = 0, 1
    while a < 10:
        print(a, end=",")
        a, b = b, a + b


def while_advanced():
    """
    walrus operator in a while loop
    """
    x = 0
    while (x := x + 1) < 10:        # NOTE: eval expr -> assign -> compare
        print(x, end=" ")
    print()


def advanced_loops():
    """
    Prerequisites: data structures
    """

    # looping through a dict
    my_dict = {"id": 2, "name": "Vik", "email": "vik.geerawor@email.com"}
    for k, v in my_dict.items():
        print(f"{k}: {v}")

    my_list = ["tic", "tac", "toe"]
    for i, v in enumerate(my_list):
        print(f"{i}. {v}")

    for item in reversed(my_list):
        print(f"{item}")

    shopping_list = ["banana", "apple", "coconut", "mango", "strawberry"]
    print(f"Shopping list: {shopping_list}")
    # NOTE: Not in place
    print(f"Shopping list (sorted): {sorted(shopping_list)}")

    shopping_list.append("banana")
    print(f"Shopping list (2 bananas): {shopping_list}")
    print(f"Shopping list (dedupe): {sorted(set(shopping_list))}")


if __name__ == "__main__":
    # fibonacci_series()
    # for_loop()
    # break_statement()
    # continue_statement()
    while_advanced()
    # advanced_loops()
