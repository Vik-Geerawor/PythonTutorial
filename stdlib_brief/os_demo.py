import os


def os_demo():
    """
    functions for interacting with the operating system
    """
    print(f"getcwd: {os.getcwd()}")
    os.chdir('stdlib')
    print(f"after chdir: {os.getcwd()}")
    # NOTE: executes the string in the sys shell
    os.system('touch test_file.txt')
    # NOTE: returns a list of all module funcs
    print(f"{dir(os)}")
    print(f"{help(os)}")


if __name__ == '__main__':
    os_demo()
