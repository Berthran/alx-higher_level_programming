#!/bin/bash
# Sends a POST request to the URL passed as argument, displays the body of the response and sets some variables
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" $1
