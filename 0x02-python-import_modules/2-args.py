#!/usr/bin/python3
def arg_printer(argv):
    cnt = len(sys.argv) - 1
    if cnt == 0:
        print("0 arguments.")
    elif cnt == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(cnt))
    for index in range(cnt):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))

if __name__ == "__main__":
    import sys
    arg_printer(sys.argv)
