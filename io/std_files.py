import sys


def std_files():
    # sys.stdout.write("What's your name: ")      # NOTE: doesn't work as expected
    # name = sys.stdin.readline()
    # print(f"Your name is {name}")

    # NOTE: Probably save in a Global Var if redirection is needed
    sout = sys.__stdout__
    sin = sys.__stdin__
    serr = sys.__stderr__
    print(f"{sout=}")
    print(f"{sin=}")
    print(f"{serr=}")
