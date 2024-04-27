#!/bin/bash

# Display the body only of a 200 status code
curl -sX "$1" -L 200
