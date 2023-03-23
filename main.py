import sys
# from operators import main
# from strings import main
# from conditionals import main
# from loops import main
# from functions import main
# from datastructures.lists import main
# from datastructures.deques import main
# from datastructures.tuples import main
# from datastructures.sets import main
# from datastructures.dictionaries import main
# from module.fibo import fib
from packages.one.hello import greet
from utilities.perfmon import timer


if __name__ == '__main__':
    # print(f'\nsys.argv = {sys.argv}')
    # main()

    # fib(10)

    # greet()

    @timer
    def waste_some_time(num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(10000)])

    waste_some_time(1000)

# 6. Modules
