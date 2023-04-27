from os import system


def builtin_objects():
    l = [1, 2, 3]

    # NOTE: same as print(l.__dir__())
    # print(dir(l))

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
        return f"Human({self.name}, {self.dob}, {self.gender})"


if __name__ == '__main__':
    system('clear')

    # builtin_objects()

    john = Human('John', '1973-10-23', 'M')
    print(f"Object: {john}")                    # NOTE: state of object
    print(f"John's state: {vars(john)}")         # NOTE: state as dict

    amy = Human('Amy', '2002-02-21', 'F')
    print(f"\nObject: {amy}")
    print(f"Amy's state: {vars(amy)}")         # NOTE: state as dict

    vik = Human
    Human.__init__(vik, 'Vik', '1981-10-15', 'M')
    print(f"\nObject: {vik}")
    print(f"Vik's state: {vars(vik)}")

    print(f"\nJohn's feed method: {type(john).feed}")
    print(f"Amy's feed method: {type(amy).feed}")
    # print(f"Vik's feed method: {type(vik).feed}")       # ERROR: feed not found
