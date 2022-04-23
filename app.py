import requests
import os

class getapi:
    def __init__(self):
        self.googleurl = os.getenv("REQ_URL")

    def google(self):
        return requests.get(self.googleurl).text

request = getapi()
print(request.google())

   