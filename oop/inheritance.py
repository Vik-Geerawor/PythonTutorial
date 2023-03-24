class Shape:
    """
    Description: Inheritance
    Assumption: 2D shapes only
    """

    # class vars

    def __init__(self, name: str) -> None:
        self.name = name


class Rectangle(Shape):
    """
    Inherits from class Shape
    """
    # class vars

    def __init__(self, name: str, length: float, width: float) -> None:
        super().__init__(name)          # TODO: super() refers to the parent
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


s = Shape(f"my star")
print(f"my shape's name: {s.name}")

r = Rectangle("my_rect", 2, 3)
print(f"Area of {r.name} = {r.get_area()}")
