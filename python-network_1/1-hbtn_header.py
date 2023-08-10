# Import the requests module for making HTTP requests
import requests
import sys

# Get the URL from the command-line argument
url = sys.argv[1]

# Send a GET request to the specified URL
response = requests.get(url)

# Get the value of the X-Request-Id header from the response
request_id = response.headers.get('X-Request-Id')

# Print the value of the X-Request-Id header
if __name__ == "__main__":
    print(request_id)