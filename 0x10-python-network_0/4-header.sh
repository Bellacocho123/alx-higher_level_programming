#!/bin/bash
# sends a get request to the URL, and displays the body of the response
curl -sL "$1" -H "X-School-User-Id: 98"
