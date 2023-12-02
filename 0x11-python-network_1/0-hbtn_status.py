#!/usr/bin/python3
"""
Fetches & displays information about status of https://alx-intranet.hbtn.io
"""

import urllib.request


def fetch_and_display_status():
    """
    Function to fetch and display information about the status
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", utf8_content)


if __name__ == "__main__":
    fetch_and_display_status()
