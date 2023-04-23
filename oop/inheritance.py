from curses.ascii import isalnum


class Animal:

    def __init__(self, name: str):
        for c in name:
            if not isalnum(c):
                raise ValueError("Name must contain alphanumeric characters only.")
        
        self.name = name

            

    def feed(self):
        print(f"{self.name} is feeding")

    def move(self):
        print(f"{self.name} is moving")


class Bird(Animal):
    def __init__(self, name):
        # NOTE: leverage super()'s validation
        super().__init__(name)

    # NOTE: Override parent method
    def feed(self):
        print(f"{self.name} is pecking.")   # that's how bird feed

    def move(self):
        print(f"{self.name} is flying.")


if __name__ == '__main__':
    a = Animal("Unknown_")
    a.feed()
    a.move()

    sparrow = Bird("Sparrow")
    sparrow.feed()
    sparrow.move()
