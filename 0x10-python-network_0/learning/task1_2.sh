#!/bin/bash
curl -s -L -w "%{http_code}" "$1" | awk '/200/{flag=1;next}/^[0-9]+$/{flag=0}flag'
