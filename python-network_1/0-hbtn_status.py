"""
dlxcbv ll;fv
"""

import requests

response = requests.get("https://alu-intranet.hbtn.io/status")
if __name__ == "__main__":
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))