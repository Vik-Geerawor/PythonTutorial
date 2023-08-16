import os
import time


def get_cwd():
    """Returns current working directory."""
    pwd = os.getcwd()
    return pwd


def get_content(my_path):
    """Returns the content on a path."""
    if os.path.isdir(my_path):          # NOTE: isdir needs abs path
        files = os.listdir(my_path)
        return files


def get_abs_content(my_path):
    """Returns the absolute path of the content on a path."""
    files = get_content(my_path)
    files = [os.path.abspath(file) for file in files]
    return files


def get_dirs(my_path):
    """Returns the directories on a path"""
    dirs = [file for file in get_abs_content(my_path) if os.path.isdir(file)]
    return dirs


def get_files(my_path):
    """Returns the regular files on a path"""
    files = [file for file in get_abs_content(my_path) if os.path.isfile(file)]
    return files


def get_file_updatetime(my_file):
    """Returns the update timestamp of a file"""
    update_timestamp = os.path.getmtime(my_file)
    update_timestamp = time.gmtime(update_timestamp)
    update_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', update_timestamp)
    return (update_timestamp, my_file)


if __name__ == '__main__':
    print(f"*** Current Directory ***")
    my_path = get_cwd()
    print(f"{my_path}")

    print(f"*** Contents ***")
    contents = get_files(my_path)
    for item in contents:
        print(f"{item}")

    print(f"*** Absolute Contents ***")
    contents = get_abs_content(my_path)
    for item in contents:
        print(f"{item}")

    print(f"*** Directories ***")
    dirs = get_dirs(my_path)
    for dir in dirs:
        print(f"{dir}")

    print(f"*** Files ***")
    files = get_files(my_path)
    for item in files:
        print(f"{item}")

    print(f"*** Update Timestamp ***")
    update_timestamp, my_file = get_file_updatetime(files[0])
    print(f"{update_timestamp} - {my_file}")
