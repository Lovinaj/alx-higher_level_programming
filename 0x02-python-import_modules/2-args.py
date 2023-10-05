#!/usr/bin/python3

import sys


def args(argv):
    argc = len(sys.argv) - 1

    if argc == 0:
        print('{:d} arguments.'.format(argc))
    elif argc == 1:
        print('{:d} argument:'.format(argc))
        print('{:d}: {:s}'.format(argc, sys.argv[argc]))
    else:
        print('{:d} argument:'.format(argc))
        for i in range(1, argc + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))


if __name__ == "__main__":
    args(sys.argv)
