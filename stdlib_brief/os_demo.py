import os


def get_cwd():
    """Return current working directory."""
    pwd = os.getcwd()
    return pwd


def get_files(my_path):
    """Return the content on a path."""
    if os.path.isdir(my_path):          # NOTE: isdir needs abs path
        files = os.listdir(my_path)
        return files


def get_files_abs(my_path):
    """Return the absolute path of the content on a path."""
    files = get_files(my_path)
    files = [os.path.abspath(file) for file in files]
    return files


def get_dirs(my_path):
    """Return the directories on a path"""
    dirs = [file for file in get_files_abs(my_path) if os.path.isdir(file)]
    return dirs


if __name__ == '__main__':
    print(f"*** Current Directory ***")
    my_path = get_cwd()
    print(f"current directory: {my_path}")

    print(f"*** Files ***")
    # files = get_files(my_path)
    # for file in files:
    #     print(f"{file}")

    files = get_files_abs(my_path)
    for file in files:
        print(f"{file}")

    print(f"*** Directories ***")
    dirs = get_dirs(my_path)
    for dir in dirs:
        print(f"{dir}")
