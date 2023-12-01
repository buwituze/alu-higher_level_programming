#!/bin/bash 
# Bashscript that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -o /dev/null -w "Status code: %{http_code}\n" "$1"
