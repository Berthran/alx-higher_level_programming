#!/bin/bash
# Displays all HTTP methos the server will accept from a URL passed as argument
curl -s -I $1 | grep -i "^allow" | awk -F': ' '{print $2}'
