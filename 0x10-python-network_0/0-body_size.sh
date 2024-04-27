#!/bin/bash

# Check if the user provided a URL argument
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Store the URL provided by the user
url=$1

# Send a GET request to the URL and store the response body
body_size=$(curl -sI "$url" | grep -i "content-length" | awk '{print $2}' | tr -d '\r')

# Check if Content-Length header is present in the response
if [ -z "$body_size" ]; then
	echo "Content-Length header not found in the response."
    else
	    echo "Body size of the response from $url: $body_size bytes"
fi
