import zlib


def compression_demo():
    s = b'witch which has which witches wrist watch'
    print(f"{len(s)} bytes")

    print(f"checksum: {zlib.crc32(s)}")

    t = zlib.compress(s)
    print(f"Post comp: {len(t)} bytes")

    u = zlib.decompress(t)
    print(f"{u}")

    print(f"checksum: {zlib.crc32(u)}")


compression_demo()
