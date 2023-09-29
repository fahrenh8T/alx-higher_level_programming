#!/usr/bin/python3
""" script takes in a URL, sends a request
    displays the value=X-Request-Id variable
    found in the header of the response
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    sent = urllib.request.Request(url)
    with urllib.request.urlopen(sent) as response:
        print(dict(response.headers).get("X-Request-Id"))
