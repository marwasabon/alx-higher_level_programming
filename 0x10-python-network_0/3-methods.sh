#!/bin/bash
# display all HTTP methods.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
