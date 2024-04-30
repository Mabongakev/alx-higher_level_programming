#!/usr/bin/python3

"""
Takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header.

Requirements:
    - Use the packages requests and sys
    - Not allowed to import packages other than reqiests and sys
    - The value of the variable is changes with each request
    - You may not check arguments passed to the script
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    req = requests.get(url)

    if req.ok:
        try:
            print(req.headers['X-Request-Id'])
        except KeyError:
            pass
