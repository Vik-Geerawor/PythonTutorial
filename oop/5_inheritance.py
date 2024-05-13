class StackInheritance(list):
    """
    Inheritance - attributes and methods are copied to derived class
    'is a' relation - StackInheritance is a list
    Inheritance from builtin types - use collections --> UserDict, UserList and UserString
    """

    def push(self, item):
        self.append(item)


class StackComposition:
    """
    Composition is preferred over Inheritance
    'has a' relationship - StackComposition has a list
    """

    def __init__(self):
        self._items = list()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)


class StackDependencyInjection:
    """
    Dependency Injection promotes loose coupling of components
    'has a' relation - StackDependencyInjection has a container
    where a container is passed/injected at the time of instantiation
    """

    def __init__(self, *, container=None):
        if container is None:
            container = list()
        self._items = container

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)
