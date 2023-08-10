"""
    Retrieves the user ID for the given GitHub username using Basic Authentication.

    Args:
        username (str): The GitHub username.
        password (str): The personal access token as the password.

    Returns:
        str: The user ID if successful, or None if authentication fails or an error occurs.
    """
import requests
import sys


def get_user_id(username, password):
    """
    Retrieves the user ID for the given GitHub username using Basic Authentication.

    Args:
        username (str): The GitHub username.
        password (str): The personal access token as the password.

    Returns:
        str: The user ID if successful, or None if authentication fails or an error occurs.
    """
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        return response.json().get('id')
    else:
        return None


# Get the GitHub username and personal access token from the command-line arguments
username = sys.argv[1]
password = sys.argv[2]

# Retrieve the user ID and display it
user_id = get_user_id(username, password)
print(user_id)
