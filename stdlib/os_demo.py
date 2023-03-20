import os
import shutil
import glob
import sys
import argparse
import re


def os_demo():
    """
    functions for interacting with the operating system
    """
    print(f"cwd: {os.getcwd()}")
    os.chdir('stdlib')
    print(f"chdir: {os.getcwd()}")
    # NOTE: executes the string in the sys shell
    os.system('touch test_file.txt')
    # NOTE: returns a list of all module funcs
    print(f"{dir(os)}")
    print(f"{help(os)}")


os_demo()
