!/usr/bin/python3
# a script that fetches a URL
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    req_page = response.read()

