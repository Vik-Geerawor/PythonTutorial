import sys


def test_python_path():
    print(f"\n*** Printing entries in sys.path ***")
    for path in sys.path:
        print(path)
    print(f"{len(sys.path)=}")

    # now run the below
    # env PYTHONPATH=/my/abs/path/to/src python module/python_path.py


if __name__ == '__main__':
    test_python_path()
