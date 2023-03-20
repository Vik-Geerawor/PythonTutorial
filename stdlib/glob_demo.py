import glob


def glob_demo():
    """
    used for searching for files
    """
    for file in glob.glob('files/*.txt'):
        print(file)
