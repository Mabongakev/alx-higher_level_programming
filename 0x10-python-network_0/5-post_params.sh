#!/bin/bash
# sends a POST request to the passed URL and variable must be email and with a test email
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
