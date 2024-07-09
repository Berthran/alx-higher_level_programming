#!/bin/bash
# Takes a URL as argument, sends a GET request and displays the body of the response
curl -s -X GET "$1"
