#!/usr/bin/python3
def add_arg(argv):
    cnt = len(argv) - 1
    if cnt == 0:
        print("{:d}".format(cnt))
        return
    else:
        r = 1
        add = 0
        while r <= cnt:
            add += int(argv[r])
            r += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
