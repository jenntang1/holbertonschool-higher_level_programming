#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for iterate in names:
        if iterate[0] != "_":
            print(iterate)
