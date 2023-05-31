def main(argv):
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
    inputfile = argv[0]
    outputfile = argv[1]

    # further processing


if __name__ == '__main__':
    import sys
    main(sys.argv)
