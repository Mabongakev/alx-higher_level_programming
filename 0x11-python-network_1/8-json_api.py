#!/usr/bin/python3

"""
Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user

Requirements:
    - The letter must be sent in the variable q
    - If no argument is given, set q=""
    - If the response body is properly JSON formatted
      and not empty, display the id and name like this: [<id>] <name>
    - Otherwise:
        - Display Not a valid JSON if the JSON is invalid
        - Display No result if the JSON is empty
    - You must use the package requests and sys
    - You are not allowed to import packages other than requests and sys
"""

if __name__ == '__main__':
    import sys
    import requests

    para = {'q': ""}

    if len(sys.argv) == 2:
        para['q'] = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'

    respo = requests.post(url, data=para)

    try:
        resp_content = respo.json()
        if resp_content == {}:
            print('No result')
        else:
            print(f'[{resp_content["id"]}] {resp_content["name"]}')
    except ValueError:
        print('Not a valid JSON')
