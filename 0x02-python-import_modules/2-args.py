#!/usr/bin/python3
def arg_printer(argv):
    cnt = len(argv) - 1
    if cnt == 0:
        print("{:d} argument.".format(cnt))
        return
    else:
        if cnt == 1:
            print("{:d} argument:".format(cnt))
        else:
            print("{:d} argument:".format(cnt))
        
        i = 1
        while i <= cnt:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    arg_printer(sys.argv)
