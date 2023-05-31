from reprlib import repr
from pprint import pprint
from textwrap import fill
import locale


def reprlib_demo():
    """
    Usage: abbreviation using elipses
    """
    r = repr(set('supercalifragilisticexpialidocious'))
    print(r)


def pprint_demo():
    t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
                                                            'yellow'], 'blue']]]

    pprint(t, width=80)


def textwrap_demo():
    doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

    print(fill(doc, width=80))


def locale_demo():
    # NOTE: Change locale - to US
    locale.setlocale(locale.LC_ALL, 'en_US')

    print(f"Locale = US")
    conv = locale.localeconv()      # NOTE: get conventions
    for k, v in conv.items():
        print(f"\t{k} = {v}")

    x = 1234567.8
    # x = locale.format_string("%d", x, grouping=True)
    x = locale.format_string("%s%.*f", (conv['currency_symbol'],
                                        conv['frac_digits'], x),
                             grouping=True)
    print(x)


# reprlib_demo()
# pprint_demo()
# textwrap_demo()
locale_demo()
