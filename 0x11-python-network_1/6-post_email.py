#!/usr/bin/python3

"""
A script that takes in a URL and an email address,
sends a POST request to the passed URL with the email
and displays the body of the response

Requirements:
    - The email must be sent in the email variable
    - You must use the packages requests and sys
    - Not allowed to import packages other than requests and sys
    - No need to check arguments passed to the script (number or type)
"""

if __name__ == '__main__':
    import sys
    import requests

    URL = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    req = requests.post(URL, data=payload)
    print(req.text)
