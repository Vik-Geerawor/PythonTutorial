def make_init(*names):
    parms = ','.join(names)
    code = f'def __init__(self, {parms}):\n'
    for name in names:
        code += f' self.{name} = {name}\n'
    d = {}
    # NOTE: exec(<code>, <globs>, <locs>)
    exec(code, d)
    return d['__init__']


class Vector:
    __init__ = make_init('x', 'y', 'z')


def main():
    v = Vector(1, 2, 3)
    print(v.x, v.y, v.z)
    print(globals())


main()
