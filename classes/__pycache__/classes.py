class MyClass:
    # NOTE: class vars
    class_type = "MyClass"

    # NOTE: constructor
    def __init__(self, name) -> None:
        # NOTE: instance vars
        self.name = name


class SubClass(MyClass):
    # class vars

    # constructor
    def __init__(self, id, name):
        # instance vars
        super().__init__(name)
        self.id = id


if __name__ == "__main__":
    a = MyClass("Tom")
    b = SubClass(1, "Tim")

    print(f"Type: {a.class_type}, Name: {a.name}")
    print(f"Type: {b.class_type}, Name: {b.name}, ID: {b.id}")
