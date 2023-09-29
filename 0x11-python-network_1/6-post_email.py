#!/usr/bin/python3
""" script takes <URL> <email>, sends a POST request to the
    passed URL with the email as a parameter & finally displays the body
    of the response

    usage: ./6-post_email.py <URL> <email>
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    quest = requests.post(url, data=value)

    print(quest.text)
