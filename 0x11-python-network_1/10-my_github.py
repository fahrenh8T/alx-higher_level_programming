#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
    uses the GitHub API to display your id

    usage: ./10-my_github.py <usrname><passwrd>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    host = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    quest = requests.get("https://api.github.com/user", auth=host)
    print(quest.json().get("id"))
