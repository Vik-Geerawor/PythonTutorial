"""
ABC allows us to create an interface
The body of an interface must contain at least one abstract class method
An abstract class method:
1. is declared with an @abstractclassmethod decorator
2. has a signature
3. is not implementated
It forces its subclasses to implement all of its abstract class methods
ABC can have fully implemented methods which can be called by its subclass
Usage:
1. type-checking
2. mixin classes
"""
from os import system
from abc import ABC, abstractclassmethod


class Person(ABC):
    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def feed(self):
        pass

    def greet(self):
        print(f"{type(self).__name__} says Hello!")


class Tom(Person):
    def __init__(self):
        pass

    def move(self):
        print(f"{type(self).__name__} is waddling.")

    def feed(self):
        print(f"{type(self).__name__} is wolfing.")


if __name__ == '__main__':
    system('clear')

    t = Tom()
    t.move()
    t.feed()
    t.greet()
