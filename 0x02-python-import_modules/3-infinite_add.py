#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    sum = 0
    argv = sys.argv
    for i in argv[1:]:
        sum += int(i)
    print(sum)
