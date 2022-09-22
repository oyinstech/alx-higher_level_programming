#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = 0
    for s in argv[1:]:
        n += int(s)
    print("{:d}".format(n))
