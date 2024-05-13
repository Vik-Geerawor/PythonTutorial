import os
import sys
from pathlib import Path


def read_only(file):
    with open(file, 'r', encoding="utf-8") as f:
        data = f.read()
        for line in data:
            print(line, end="")


def write_only(file):
    with open(file, 'w', encoding="utf-8") as f:
        for i in range(5):
            f.write(f"Line {i} written by system\n")

    read_only(file)


def append_only(file):
    with open(file, 'a', encoding="utf-8") as f:
        for i in range(5):
            f.write(f"Line {i} appended by system\n")

    read_only(file)


def read_write(file):
    with open(file, 'r+', encoding="utf-8") as f:
        for i in range(5):
            f.write(f"Line {i} written in RW mode\n")

        data = f.read()
        for line in data:
            print(line, end="")


def read_line(file):
    with open(file, 'r', encoding="utf-8") as f:
        while (line := f.readline()):
            print(line, end="")
        print("")


def recommended_reading(file):
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            print(f"{line}", end="")


def file_tell(file):
    """
    Returns the current position of pointer
    """
    with open(file, 'r', encoding="utf-8") as f:
        while (char := f.read(1)):      # tell starts at 0, after read it's 1
            if char == '\n':
                char = r'\n'
            print(f"{f.tell() - 1:>2d} - {char}")   # hence the -1


def file_seek(file):
    """
    Seeks to a new file position
    """
    with open(file, 'r', encoding="utf-8") as f:
        # print(f"Cursor Position: {f.tell()}")

        # print(f.readline(), end="")
        # print(f"Position: {f.tell()}")

        # f.seek(0)
        # print(f"Position after seek: {f.tell()}")
        # print(f.readline(), end="")

        # print(f"Reading first char: {f.read(1)}")
        print(f"Cursor Position: {f.tell()}")
        print(f"f.seek(1, os.SEEK_CUR)")
        f.seek(1, os.SEEK_CUR)
        print(f"Reading first char: {f.read(1)}")
        print(f"Cursor Position: {f.tell()}")


def get_fs_encoding():
    """
    if filenames are in binary, we pass it as is
    """
    print(sys.getfilesystemencoding())      # NOTE: returns OS filename encoding


def get_path(file):
    """
    Representing a file as an object using pathlib
    """
    p = Path(file)
    for item in dir(p):
        print(item)

    print(p.__fspath__())


def file_methods(file):
    f = open(file)

    print(f"{f.closed=}")       # False if open
    print(f"{f.mode=}")         # r/w mode
    print(f"{f.name=}")
    print(f"{f.newlines=}")     # newline char
    print(f"{f.encoding=}")
    print(f"{f.errors=}")       # error handling policy
    print(f"{f.write_through=}")    # True if unbuffered

    f.close()


if __name__ == '__main__':
    file = 'files/test.txt'
    # read_only(file)
    # write_only(file)
    # append_only(file)
    # read_write(file)
    # read_line(file)
    # recommended_reading(file)
    # file_tell(file)
    # file_seek(file)
    # get_fs_encoding()
    # get_path(file)
    file_methods(file)
