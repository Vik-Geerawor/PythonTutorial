import inspect
import sys
from collections import ChainMap


def spam(x, y):
    z = x + y
    grok(z)


def grok(a):
    b = a * 10

    # outputs: {'a':5, 'b':50 }
    print(inspect.currentframe().f_locals)

    # outputs: {'x':2, 'y':3, 'z':5 }
    print(inspect.currentframe().f_back.f_locals)


def grok_v2(a):
    b = a * 10
    print(sys._getframe(0).f_locals)    # myself
    print(sys._getframe(1).f_locals)    # my caller


def debug(*varnames):
    f = inspect.currentframe().f_back
    vars = ChainMap(f.f_locals, f.f_globals)
    print(f'{f.f_code.co_filename}:{f.f_lineno}')
    for name in varnames:
        print(f'    {name} = {vars[name]!r}')


# Example use
def func(x, y):
    z = x + y
    debug('x', 'y')  # Shows x and y along with file/line
    return z


def main():
    spam(2, 3)
    grok(5)
    grok_v2(5)
    func(1, 2)


main()
