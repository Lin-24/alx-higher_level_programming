#!/bin/bash
# Script that takes in URL,sends GET request,displays the body if status code = 200
curl -sL "$1" -w "\n"
