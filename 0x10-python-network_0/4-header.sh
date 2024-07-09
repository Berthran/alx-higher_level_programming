#!/bin/bash
# Sens a GET request to the URL passes as an argument, displays the response's body and sends a header variable 
curl -s -H "X-School-User-Id: 98" $1
