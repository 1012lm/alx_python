"""
    Sends a request to the given URL and displays the body of the response.
    If the HTTP status code is greater than or equal to 400, prints an error code.

    Args:
        url (str): The URL to send the request to.
    """

import requests
import sys

def display_response(url):
    """
    Sends a request to the given URL and displays the body of the response.
    If the HTTP status code is greater than or equal to 400, prints an error code.

    Args:
        url (str): The URL to send the request to.
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

# Get the URL from the command-line argument
url = sys.argv[1]

# Send a request to the URL and display the response
display_response(url)