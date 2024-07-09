#!/bin/bash
# Takes a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -o /dev/null -w "%{size_download}\n" -X GET "$1"
