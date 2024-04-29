#!/bin/bash
#Display the size of the body
echo $(curl -sI "$1" | grep 'Content-Length' | cut -d ':' -f 2)
