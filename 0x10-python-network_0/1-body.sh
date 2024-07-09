#!/bin/bash
# Takes a URL as argument, sends a GET request and displays the body of the response
curl -s -L -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
