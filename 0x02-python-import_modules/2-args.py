#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    print("{:d} argument".format(len(argv) - 1), end="")
    if len(argv) == 1:
        print(".")
    elif len(argv) == 2:
        print(":")
    else:
        print("s:")

    for i in range(len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
