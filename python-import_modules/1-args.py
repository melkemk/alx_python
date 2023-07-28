#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if (len(sys.argv) - 1) == 0:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    elif (len(sys.argv) - 1) == 1:
        print("{:d} argument:".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv) - 1):
        print("{:d}: {}".format(i + 1, sys.argv[i+1]))