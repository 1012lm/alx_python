"""
    Sends a request to the given URL and displays the body of the response.
    If the HTTP status code is greater than or equal to 400, prints an error code.

    Args:
        url (str): The URL to send the request to.
    """

import requests
import sys


def search_user(letter):
    """
    Sends a request to the given URL and displays the body of the response.
    If the HTTP status code is greater than or equal to 400, prints an error code.

    Args:
        url (str): The URL to send the request to.
     """
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': letter}
    response = requests.post(url, params=params)

    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


# Get the letter from the command-line argument
letter = sys.argv[1] if len(sys.argv) > 1 else ""

# Send a POST request to the URL with the letter as a parameter
search_user(letter)
