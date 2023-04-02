class ListTransaction:
    """
    Context Manager class must have the below 2 methods:
    1. __enter__()
    2. __exit__()
    """

    def __init__(self, thelist):
        self.thelist = thelist

    def __enter__(self):
        self.workingcopy = list(self.thelist)
        return self.workingcopy

    def __exit__(self, type, value, tb):
        if type is None:
            self.thelist[:] = self.workingcopy
        return False


if __name__ == "__main__":

    items = [1, 2, 3]

    with ListTransaction(items) as working:
        working.append(4)
        working.append(5)
    print(items)       # Produces [1,2,3,4,5]

    try:
        with ListTransaction(items) as working:
            working.append(6)
            working.append(7)
            raise RuntimeError("We're hosed!")
    except RuntimeError:
        pass

    print(items)   # Produces [1,2,3,4,5]
