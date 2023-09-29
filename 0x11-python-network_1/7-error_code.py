#!/usr/bin/python3
""" sends a request to url & displays the body of the response

    usage: ./7-error_code.py <url>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    quest = requests.get(url)
    if quest.status_code >= 400:
        print("Error code: {}".format(quest.status_code))
    else:
        print(quest.text)
