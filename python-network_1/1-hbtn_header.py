"""
    Import the requests module for making HTTP requests
"""
import requests
import sys

"""
    Import the requests module for making HTTP requests
"""


def fetch_request_id(url):
    """
    Fetches the value of the X-Request-Id header from the response of the given URL.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        str: The value of the X-Request-Id header.
    """
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    return request_id

url = sys.argv[1]
request_id = fetch_request_id(url)

if __name__ == "__main__":
    print(request_id)