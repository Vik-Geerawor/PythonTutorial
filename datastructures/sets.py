def set_demo():
    """
    Usage: membership testing and eliminating duplicate entries
    """
    a = set('abracadabra')
    b = set('alacazam')

    print(f"a = {a}")
    print(f"b = {b}")

    print(f"a - b (minus) = {a - b}")   # only in a
    print(f"a | b (union) = {a | b}")   # a or b or both
    print(f"a & b (intersect) = {a & b}")   # a and b
    print(f"a ^ b (uni - inter) = {a ^ b}")   # a or b, but not both


def main():
    set_demo()
