#!/usr/bin/python3
""" takes a letter & sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as parameter

    usage: ./8-json_api.py <letter>
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    quest = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        response = quest.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
