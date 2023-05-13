import sys


def main():
    print(f"\n*** Printing entries in sys.path ***")
    for path in sys.path:
        print(path)

    """
    Manually adding a path to PYTHONPATH when executing a program
        env PYTHONPATH=/mnt/data/Projects/python/PythonTutorial \
        python module/search_path.py
    """

    # adding a zip file containing modules
    sys.path.append('/mnt/data/Projects/python/PythonTutorial/pkg.zip')
    """
    .egg files are like .zip files with additional metadata
    """
    print(f"\n-- After adding zip pkg --")
    for path in sys.path:
        print(path)


if __name__ == '__main__':
    main()
