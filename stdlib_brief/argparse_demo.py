import argparse


def argparse_demo():
    parser = argparse.ArgumentParser(
        prog='osx',
        description='test std lib modules'
    )

    parser.add_argument('my_args', nargs='+')       # NOTE: positional args
    parser.add_argument('-l', '--lines', type=int, default=10)  # NOTE: options
    parser.add_argument('-p', '--port', type=int, default=5432)
    args = parser.parse_args()

    # print(f"{type(args)} - {args}")
    print(f"positional args:")
    for i, a in enumerate(args.my_args, 1):
        print(f"\t{i}. {a}")
    print(f"option --lines: {args.lines}")
    print(f"option --port: {args.port}")


if __name__ == '__main__':
    argparse_demo()
