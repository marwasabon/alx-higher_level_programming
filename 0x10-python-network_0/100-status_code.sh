#!/bin/bash
# sends a GET req and display the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
