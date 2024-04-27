#!/bin/bash

# Check if the user provided a URL argument
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Store the URL provided by the user
url=$1

# Send a GET request to the URL and store the response body
echo $(curl -sI "$url" | grep "content-length" | cut -d ":" -f 2)
