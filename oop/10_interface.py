"""
ABC allows us to create an interface
which enforces its subclasses to implement all of them
ABC can have fully implemented methods which can be called by its subclass
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
