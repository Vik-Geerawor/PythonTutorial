import sys


def sys_demo():
    """
    parsing command line arguments
    """
    print(sys.argv)
    sys.stderr.write("Warning: Unable to connect to database!\n")