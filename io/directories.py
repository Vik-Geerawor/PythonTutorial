import os
import sys
from pathlib import Path


def ls(dir_name: str, encoding: str) -> list:
    return os.listdir(dir_name.encode(encoding))


def test_ls():
    dir_name = os.getcwd()
    encoding = sys.getfilesystemencoding()      # NOTE: system independent

    contents = ls(dir_name, encoding)
    for item in contents:
        print(item.decode(encoding))


def grep(dir_name: str, pattern: str):
    return Path(dir_name).glob(pattern)


def rgrep(dir_name: str, pattern: str):
    """
    Recursive grep
    """
    return Path(dir_name).rglob(pattern)


def test_grep():
    dir_name = os.getcwd()
    pattern = '*.py'

    files = grep(dir_name, pattern)
    if files:
        for file in files:
            print(f"{type(file)=} - {file}")


def test_rgrep():
    dir_name = os.getcwd()
    pattern = '*.py'

    files = rgrep(dir_name, pattern)
    if files:
        for file in files:
            print(f"{file}")


if __name__ == '__main__':
    # test_ls()
    test_grep()
    # test_rgrep()
