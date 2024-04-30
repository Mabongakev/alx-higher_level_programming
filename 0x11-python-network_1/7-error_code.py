#!/usr/bin/python3

"""
Python script that takes in a URL and
sends a request to the URL and displays the body of the response.

Requirements:
    - If the HTTP status code is greater than or equal to 400,
      print: Error code: followed by the value of the HTTP status code
    - Must use the packages requests and sys
    - Not allowed to import packages other than requests and sys
    - No need to check arguments passed to the script
"""

if __name__ == "__main__":
    import requests
    import sys

    URL = sys.argv[1]

    respo = requests.get(URL)

    if respo.status_code >= 400:
        print(f'Error code: {respo.status_code}')
    else:
        print(respo.text)
