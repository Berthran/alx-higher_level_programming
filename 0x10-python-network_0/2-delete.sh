#!/bin/bash
# Sends a DELETE request to the URL passed as an argument and displays the body of the response
curl -s -X DELETE "$1"
