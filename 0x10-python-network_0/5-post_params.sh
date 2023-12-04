#!/bin/bash
# Script that sends a POST request to the specified URL with specific parameters and displays the response body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
