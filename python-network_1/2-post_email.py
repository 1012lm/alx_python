"""
    vcbldsvb ,c b
"""

import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

response = requests.post(url, data=data)

if __name__ == "__main__":
    print(response.text)
