#!/usr/bin/python3
if __name__ == "__main__":
    import add_0
    a = 1
    b = 2
    add_0.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add_0.add(a, b)))
