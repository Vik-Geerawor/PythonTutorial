from os import system
import pathlib
import re


def get_paths(parent_dir, pattern):
    for path in pathlib.Path(parent_dir).rglob(pattern):
        if path.exists():
            yield path


def get_files(paths):
    for path in paths:
        with path.open('rt', encoding='utf-8') as f:
            yield f


def get_lines(files):
    for file in files:
        yield from file


def get_comments(lines):
    for line in lines:
        m = re.match('\s+.*(#.*)$', line)
        if m:
            print(m)
            yield m.group()


def print_matching(lines, substring):
    for line in lines:
        if substring in lines:
            print(substring)


if __name__ == '__main__':
    system('clear')

    pypaths = get_paths('generators', '*.py')
    pyfiles = get_files(pypaths)
    pylines = get_lines(pyfiles)
    comments = get_comments(pylines)
    print_matching(comments, 'NOTE')
