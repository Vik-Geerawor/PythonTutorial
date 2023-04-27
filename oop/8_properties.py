class Point:
    def __init__(self, x, y):
        self.x = x              # NOTE: is a call to setter func -> validated
        self.y = y

    @property
    def x(self):
        return self._x          # NOTE: is the actual name of the attribute

    @x.setter
    def x(self, x):
        if -100 <= x <= 100:
            self._x = x
        else:
            raise ValueError("X must be between -100 and 100 inclusive.")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if -100 <= y <= 100:
            self._y = y
        else:
            raise ValueError("Y must be between -100 and 100 inclusive.")

    def __str__(self) -> str:
        return f"{type(self).__name__}: ({self.x}, {self._y})"


if __name__ == '__main__':
    p1 = Point(20, 20)
    print(p1)
    p1.x = 150
    p1.y = 150
    print(p1)
