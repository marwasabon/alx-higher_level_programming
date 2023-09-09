#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    print("{:d} argument".format(len(argv) - 1), end="")
    if len(argv) == 0:
        print("0 arguments.")
    if len(argv) == 1:
        print(".")
    elif len(argv) == 2:
        print(":")
    else:
        print("s:")

    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
