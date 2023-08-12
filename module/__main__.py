"""
The parent directory can now be executed as if it were a module
This file is the entry point of the execution
command to execute is
    python module
"""

from fibo import fib, fib2

print(f"Module name: {__name__}")
fib(10)
r = fib2(10)
print(r)
