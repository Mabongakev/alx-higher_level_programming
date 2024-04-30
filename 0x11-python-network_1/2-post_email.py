#!/usr/bin/python3

"""
Python script that takes in a URL and an email, and sends POSTs
while displaying the body of the response (decoded in utf-8)

Requirements:
    - The email must be sent in the email variable
    - You must use the packages urllib and sys
    - You are not allowed to import packages other than urllib and sys
    - You don't need to check arguments passed to the script (number or type)
    - You must use the with statement
"""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email_address': email}

    data = urllib.parse.urlencode(values).encode()
    request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf8'))
