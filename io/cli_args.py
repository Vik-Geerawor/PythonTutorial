import argparse


def main_simple(argv):
    """
    Good idea to have a dedicated main() function which accepts the
    command-line args as a list.
    Call this main() function at the end of the program.
    See also 'argparse'
    """
    if len(argv) != 3:
        raise SystemExit(
            f'Usage : python {argv[0]} inputfile outputfile\n'
        )
    inputfile = argv[1]
    outputfile = argv[2]

    print(f"You passed {inputfile=} and {outputfile=}")


def main_advanced(argv):
    p = argparse.ArgumentParser(description="This is some program")

    # A positional argument
    p.add_argument("infile")        # ERROR

    # An option taking an argument
    p.add_argument("-o", "--output", action="store")

    # An option that sets a boolean flag
    p.add_argument("-d", "--debug", action="store_true",
                   default=False)  # ERROR

    # Parse the command line
    args = p.parse_args(args=argv)

    # Retrieve the option settings
    infile = args.infile
    output = args.output
    debugmode = args.debug

    print(infile, output, debugmode)


if __name__ == '__main__':
    import sys
    # main_simple(sys.argv)
    main_advanced(sys.argv)
