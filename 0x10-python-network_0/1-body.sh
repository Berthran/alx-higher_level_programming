#!/bin/bash
# Takes a URL as argument, sends a GET request and displays the body of the response
curl -s -w "%{http_code}" -L "$1" | grep -q 200 && curl -s -L "$1"
