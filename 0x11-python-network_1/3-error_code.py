#!/usr/bin/python3
""" script takes in a URL, sends a request to the URL
    displays the body of the response (decoded in utf-8)

    usage: ./3-error_code.py <url>
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
