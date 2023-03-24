class A:
    """
    A simple class example
    """

    # NOTE: Constructore
    def __init__(self, name):
        # NOTE: instance vars
        self.name = name

    def __len__(self):
        return len(self.name)

    def __repr__(self):
        return f"{type(self).__name__} at 0x{id(self):x}, size={len(self)}, name={self.name}"


a = A('motivation')

print(a)
