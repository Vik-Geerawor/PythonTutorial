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
        line = f.readline()
        while line:
            print(line, end="")
            line = f.readline()


def recommended_reading(file):
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            print(f"{line}", end="")


def file_tell(file):
    with open(file, 'r', encoding="utf-8") as f:
        print(f.tell())

        print(f.readline(), end="")
        print(f.tell())

        print(f.readline(), end="")
        print(f.readline(), end="")
        print(f.tell())


def file_seek(file):
    with open(file, 'r', encoding="utf-8") as f:
        print(f"Starting Position: {f.tell()}")

        print(f.readline(), end="")
        print(f"Position: {f.tell()}")

        f.seek(0)
        print(f"Position after seek: {f.tell()}")
        print(f.readline(), end="")


if __name__ == '__main__':
    file = 'files/test.txt'
    # read_only(file)
    # write_only(file)
    # append_only(file)
    # read_write(file)
    # read_line(file)
    # recommended_reading(file)
    # file_tell(file)
    file_seek(file)
