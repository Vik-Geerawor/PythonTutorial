from os import system


class MyClass:
    """
    A simple class example
    Rules:
    1. Instance vars are:
        a. defined in the init method
        b. are always prefixed with 'self'
    2. Instance methods take 'self' as their first parameter
    3. Class vars:
        a. are defined outside of any methods
        b. are accessed by prefixing their names with the class name
    4. Class methods:
        a. are defined with the '@classmethod' decorator
        b. have 'cls' as their first parameter
    """

    # NOTE: Class variable
    instance_counter = 0

    # NOTE: Constructor
    def __init__(self, name):
        # NOTE: instance vars
        self.name = name
        MyClass.instance_counter += 1     # NOTE: class name, not self

    # NOTE: Instance method
    def __len__(self):
        return len(self.name)

    def __repr__(self):
        return f"{type(self).__name__} at 0x{id(self):x}, size={len(self)}, name={self.name}"

    # NOTE: Class method - first arg always 'cls'
    @classmethod
    def from_file(cls, file):
        """
        Typical use of a class method
        Creates a list of instances from a file
        """
        object_list = []
        with open(file, 'rt', encoding="utf-8") as f:
            for name in f:
                object_list.append(cls(name))
        return object_list


if __name__ == '__main__':
    system('clear')
    a = MyClass('apple')
    print(a)

    b = MyClass('banana')
    print(b)

    obj_list = MyClass.from_file('files/names.txt')
    for obj in obj_list:
        if isinstance(obj, MyClass):
            print(obj, end='')
    print()
