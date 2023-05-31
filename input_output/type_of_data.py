def byte_data():
    """
    a is an array of bytes and is type class 'bytes'
    a[0] is of type class 'int'
    """
    a = b'hello'
    print(f"a type = {type(a)}")
    print(f"a[0] type = {type(a[0])}")

    for i in a:
        print(f"{i}", end=', ')
    print()

    """
    to access the text we need to
    decode the bytes using utf-8 encoding
    """
    t = a.decode('utf-8')
    print(f"t = {t} and type = {type(t)}")


def text_data():
    """
    all text data read from input must be decoded
    all text data written to output must be encode
    """
    a = input("Enter a text:")
    # a = a.decode('utf-8')
    print(a)

if __name__ == '__main__':
    # byte_data()
    text_data()



