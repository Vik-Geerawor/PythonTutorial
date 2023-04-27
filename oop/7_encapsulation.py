class A:
    def __init__(self, x):
        self._x = x        # NOTE: private attribute

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._validate_x(x)

    def _validate_x(self, x):      # NOTE: private method
        if x < 10:
            self._x = x
        else:
            raise ValueError("Value must be less 10.")


if __name__ == '__main__':
    a = A(7)
    print(a.get_x())
    # a.set_x(15)
    # print(a.get_x())
    a._validate_x(19)  # ERROR: object has no attribute
    a._A_validate_x(5)  # NOTE: mangled name, still works
