def int_to_bin(a: int) -> str:
    return bin(a)


def bin_to_int(a: str) -> int:
    return int(a, 2)


def int_to_char(a: int) -> str:
    return chr(a)


def char_to_int(a: str) -> int:
    return ord(a)


def bytes_to_str(a: bytearray) -> str:
    return a.decode('utf-8')


def str_to_bytes(a: str) -> bytes:
    return a.encode('utf-8')


def binary_data():
    a: bytes = b'hello'
    print(f"{a=} -> {type(a)=}")
    print(f"{a[0]=} -> {type(a[0])=}")

    b: bytes = b'world'
    print(f"{b=} -> {type(b)=}")

    c: bytearray = bytearray()
    c.extend(a)
    print(f"{c=} -> {type(c)=}")
    c.extend(b)
    print(f"{c=} -> {type(c)=}")

    d = int_to_bin(a[0])
    print(f"{d=} -> {type(d)=}")

    e = bin_to_int(d)
    print(f"{e=} -> {type(e)=}")

    f = int_to_char(e)
    print(f"{f=} -> {type(f)=}")

    g = bytes_to_str(c)
    print(f"{g=} -> {type(g)=}")

    h = str_to_bytes(g)
    print(f"{h=} -> {type(h)=}")


def read_image():
    filename = 'files/PythonIcon.png'
    with open(filename, 'rb') as f:
        bin_data = f.read()
        print(f"{type(bin_data)=}")
        print(bin_data)


def text_data():
    """
    all text data read from input must be decoded
    all text data written to output must be encode
    """
    a = input("Enter a text:")
    # a = a.decode('utf-8')
    print(a)


if __name__ == '__main__':
    # binary_data()
    # text_data()
    read_image()
