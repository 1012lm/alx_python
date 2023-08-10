"""
    Sends a request to the given URL and displays the body of the response.
    If the HTTP status code is greater than or equal to 400, prints an error code.

    Args:
        url (str): The URL to send the request to.
    """
import requests
import sys


def display_user_info(response):
    """
    Sends a request to the given URL and displays the body of the response.
    If the HTTP status code is greater than or equal to 400, prints an error code.

    Args:
        url (str): The URL to send the request to.
    """
    try:
        data = response.json()
        if data:
            user_info = f"[{data.get('id')}] {data.get('name')}"
            print(user_info)
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


def search_user(letter):
    """
    Sends a request to the given URL and displays the body of the response.
    If the HTTP status code is greater than or equal to 400, prints an error code.

    Args:
        url (str): The URL to send the request to.
    """
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}
    response = requests.post(url, data=params)
    status_code = response.status_code
    if status_code >= 400:
        print(f"Error code: {status_code}")
    else:
        display_user_info(response)


# Get the letter from the command-line argument
letter = sys.argv[1] if len(sys.argv) > 1 else ""

# Send a POST request to the URL with the letter as a parameter
search_user(letter)
