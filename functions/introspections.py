import inspect


def add(x: int, y: int) -> int:
    def do_add():
        return x + y
    return do_add


sig = inspect.signature(add)

print(sig)

'''
$ python
>>>
from functions import introspections
dir(introspections)
a = introspections.add(1, 2)
dir(a)
a.__closure__
a.__closure__[0].cell_contents
'''
