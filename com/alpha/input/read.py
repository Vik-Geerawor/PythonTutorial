__all__ = ['read_data']


def read_data(source, handle):
    if source == "file":
        from .from_file import read_file
        read_file(source, handle)
    elif source == "database":
        from .from_db import read_db
        read_db(source, handle)
    elif source == "internet":
        from .from_internet import read_internet
        read_internet(source, handle)


def read_file(*args, **kwargs):
    print(f"running {__name__}")
    print("Reading data from file")


def read_db(*args, **kwargs):
    print(f"running {__name__}")
    print("Reading data from database")


def read_internet(*args, **kwargs):
    print(f"running {__name__}")
    print("Reading data from internet")
