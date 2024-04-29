#!/usr/bin/bash
# sends a GET request to the URL with a header variable X-School-User-Id and value 98
curl -sL "$1" -H "X-School-User-Id: 98"
