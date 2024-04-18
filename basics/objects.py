from os import system


def object_id(obj):
    """
    ID of an object never changes once created
    """
    return id(obj)


def object_type(obj):
    """
    Type of an object never changes once created
    """
    return type(obj)


def object_value(obj):
    """
    Value of an object can change
    """
    return obj


if __name__ == "__main__":
    # clear screen
    system("clear")

    a: int = 2
    a_id = object_id(a)
    print(f"ID of a: {a_id}")

    a_type = object_type(a)
    print(f"Type of a: {a_type}")

    a_value = object_value(a)
    print(f"Value of a: {a_value}")
