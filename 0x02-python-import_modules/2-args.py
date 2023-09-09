#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n_argv = len(argv) - 1

    if n_argv == 0:
        print("0 arguments.")
    else:
        print("{:d} argument".format(n_argv), end="")
        if n_argv == 1:
            print(".")
        elif n_argv == 2:
            print("s:")
        else:
            print("s:")
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
