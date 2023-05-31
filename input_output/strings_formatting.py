def f_strings():
    year = 2016
    event = 'Referendum'

    print(f"Results of the {year} {event}")


def format_string():
    yes_votes = 42_572_654
    no_votes = 43_132_495

    percentage = yes_votes / (yes_votes + no_votes)
    percentage = 0.02

    # print("{:-9} YES votes {:2.2%}".format(yes_votes, percentage))

    # NOTE: > justified, 10 chars, [d=integer, f=float, %=percent, s=string]
    print(f"{yes_votes:>10d} YES votes {percentage:>10.2%}")


if __name__ == '__main__':
    # f_strings()
    format_string()
