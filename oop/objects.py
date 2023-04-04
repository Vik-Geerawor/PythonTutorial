from os import system


def builtin_objects():
    l = [1, 2, 3]

    # print(dir(l))       # NOTE: same as print(l.__dir__())

    for i in dir(l):
        print(f"{i} - {type(i)}")


class Human:
    """
    A class to represent a human being
    """

    def __init__(self, name, dob, gender) -> None:
        """
        The constructor
        """
        self.name = name
        self.dob = dob
        self.gender = gender

    def feed(food):
        print(f"Eating {food}.")

    def sleep(num):
        print(f"Slept {num} hours.")

    def work(num):
        print(f"Working really hard for {num} hours.")

    def __repr__(self) -> str:
        return f"Human({self.name!r}, {self.dob!r}, {self.gender!r})"


if __name__ == '__main__':
    system('clear')

    # builtin_objects()

    john = Human('John', '1973-10-23', 'M')
    print(f"Object: {john}")             # NOTE: state of object
    print(f"John's vars: {vars(john)}")       # NOTE: vars of object

    amy = Human('Amy', '2002-02-21', 'F')
    print(f"\nObject: {amy}")

    # NOTE: all methods are class methods
    print(f"\nJohn's feed method: {type(john).feed}")
    print(f"Amy's feed method: {type(amy).feed}")
