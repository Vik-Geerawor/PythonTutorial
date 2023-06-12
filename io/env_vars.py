"""
Data can be passed to a program via env variables
set in the command shell.
e.g. env VAR=value python program.py
the values are accessed via 'os.environ'
"""

import os


def show_environ():
    for k, v in os.environ.items():
        # print(f'{k} = {v}')
        if k == 'PYTHONPATH':
            """
            run: env PYTHONPATH='/TestPath/PythonTutorial' python io/env_vars.py
            """
            print(f"Found it: {k} = {v}")

    # user = os.environ['USER']
    # print(user)

    # path = os.environ['PATH']
    # print(path)


if __name__ == '__main__':
    show_environ()
