#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = []
    for iterate in argv[1:]:
        add.append(int(iterate))
    print(sum(add))
