#!/usr/bin/python3
'''module: 101-stats
    reads from standard input and computes metrics
'''


def print_stats(size, status_codes):
    '''function: print_stats
        Print accumulated metrics

        Args:
            fl_size (int): total file size
            status_codes (dict): dictionary containing
                the count of each status code
    '''
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    fl_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_cnt = 0

    try:
        for line in sys.stdin:
            if line_cnt == 10:
                print_stats(fl_size, status_codes)
                line_cnt = 1
            else:
                line_cnt += 1

            line = line.split()

            try:
                fl_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(fl_size, status_codes)

    except KeyboardInterrupt:
        print_stats(fl_size, status_codes)
        raise
