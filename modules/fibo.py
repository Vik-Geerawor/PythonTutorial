"""
Python searches for a module using:
1. sys.builtin_module_names - var containing a tuple of names of builtin modules
2. sys.path - var containing a list of directories containing .py files
    a. dir of the input script
    b. PYTHONPATH - python env var similar to PATH env var
    c. installation default, e.g. site-packages

__pycache__
a. cache of compiled code used to load modules
b. to run compiled code add .pyc to source directory and .py file
c. cache is ignored (1) for modules loaded from CLI (ii) when there is no .py file

dir([<module_name>])
a. list the names of objects - vars, modules, funcs, etc

from pkg1.pkg2...pkgn import [pkg | module | func | class | var]
"""


# Fibonacci numbers module

def fib(n):
    """
    Description: prints Fibonacci series upto n
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    """
    Description: returns Fibonacci series upto n
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b

    return result


if __name__ == "__main__":
    """
    Description: This makes this module executable as a script
    """

    import sys
    fib(int(sys.argv[1]))       # NOTE: 2nd arg of the interpreter

# python modules/fibo.py 10
# 0 1 1 2 3 5 8
