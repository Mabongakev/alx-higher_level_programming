#!/usr/bin/python3

"""
Fetches https://alx-intranet.hbtn.io/status

Requirements:
    - Use the package requests
    - You are not allow to import packages other than requests
    - The body of the response must be display eg (tabulation before -)
"""

if __name__ == '__main__':
    from requests import get

    req = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(req.text)}')
    print(f'\t- content: {req.text}')
