#!/usr/bin/python3
""" displays the X-Request-Id header variable of a request
    to a given URL

    usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    quest = requests.get(url)
    print(quest.headers.get("X-Request-Id"))
