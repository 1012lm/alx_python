"""
hjsv;v  lufg;v fv
"""


import requests
import sys

url = sys.argv[1]

response = requests.get(url)
request_id = response.headers.get('X-Request-Id')
if __name__ == "__main__":
    print(request_id)