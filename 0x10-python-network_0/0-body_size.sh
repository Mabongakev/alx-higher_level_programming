#!/bin/bash

# Check if the user provided a URL argument
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send a GET request to the URL and store the response body
echo $(curl -sI "$1" | grep "Content-Length" | cut -d ":" -f 2)
