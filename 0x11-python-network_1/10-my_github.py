#!/usr/bin/python3
"""
Script to authenticate with GitHub API using a personal access token
and display user ID.
"""

import requests
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    access_token = sys.argv[2]
    api_url = "https://api.github.com/user"
    headers = {
            'Authorization': f'token {access_token}'
            }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info['id']
        print(user_id)
    else:
        print("None")
