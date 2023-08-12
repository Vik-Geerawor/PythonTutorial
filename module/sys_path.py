import sys


def test_sys_path():
    print(f"\n*** Printing entries in sys.path ***")
    for path in sys.path:
        print(path)

    # manually adding a zip file containing modules
    sys.path.append('/my/abs/path/to/pkg.zip')

    print(f"\n-- After adding pkg.zip --")
    for path in sys.path:
        print(path)


if __name__ == '__main__':
    test_sys_path()
