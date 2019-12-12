#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add as A
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, A(a, b)))
