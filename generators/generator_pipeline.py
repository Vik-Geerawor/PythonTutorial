from os import system
import math


def read_file(file):
    """
    Memory efficient file reading and processing data
    to show the generation expression pipeline which can be used
    to process a huge file
    """
    with open(file, 'rt') as f:
        lines = (line for line in f)
        line = (line.partition('#')[0].strip() for line in lines if line)
        # remove blank lines
        data = (float(col) for col in line if col != '')
        data = (num for num in data if math.isfinite(num))
        data = ((max(0., num)) for num in data)
        s = sum(data)
        return s


if __name__ == '__main__':
    system('clear')

    file = 'files/data.csv'
    r = read_file(file)
    print(r)


# https://www.youtube.com/watch?v=tmeKsb2Fras
