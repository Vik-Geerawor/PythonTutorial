# Normal classes


class ClassA:
    def some_method(self):
        print("Running A.some_method")


class ClassB:
    def some_method(self):
        print("Running B.some_method")


# Mixin class
class MixinClassOne:
    def some_method(self):
        return super().some_method()


# Multiple Inheritance
class ChildA(MixinClassOne, ClassA):
    ...


class ChildB(MixinClassOne, ClassB):
    ...


if __name__ == '__main__':
    a = ChildA()
    a.some_method()
    # NOTE:
    '''
    MRO = Method Resolution Order --> __mro__ of class
    The class with super(), i.e. MixinClassOne checks the MRO to find it's own 
    position then calls the method in the next class, i.e. ClassA in this case
    '''
    print("MRO of class ChildA")
    for item in ChildA.__mro__:
        print(item)

    print()
    b = ChildB()
    b.some_method()
    print("MRO of class ChildB")
    for item in ChildB.__mro__:
        print(item)
