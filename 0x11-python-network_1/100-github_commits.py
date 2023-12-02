#!/usr/bin/python3
"""
Script to list 10 commits (from the most recent to oldest) of a GitHub repo.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    api_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(api_url)
    if response.status_code == 200:
        for commit in response.json()[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
        else:
            print(f"Failed to retrieve commits. Status Code:
                  {response.status_code}")
            print(response.text)
