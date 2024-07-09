#!/bin/bash
status_code=$(curl -s -o /dev/null -w "%{http_code}" -L "$1")
if [ "$status_code" -eq 200 ]; then
	curl -s -L "$1"
fi
