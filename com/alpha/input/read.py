__all__ = ['read_data']


def read_data(source, handle, /):
    if source == "file":
        read_file(source, handle)
    elif source == "database":
        read_db(source, handle)
    elif source == "internet":
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
