class Reverse:
    """
    Iterable class which iterates backwards
    """

    def __init__(self, data) -> None:
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


if __name__ == "__main__":
    my_list = [3, 1, 5, 9, 4]
    r = Reverse(my_list)
    for i in r:
        print(i)
