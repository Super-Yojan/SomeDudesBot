"""
drMoscovium

Gets message from the user, and  sends it to the server
"""

import requests
import json

async def solve_chall(message):
    if "Direct Message" in str(message.channel):
        url = "http://backend:8080/solve"
        data ={
            "User": str(message.author),
            "Title": str(message.content),
            "File": str(message.attachments[0].url)
            }
        x = requests.post(url, json=data)
        print(x.json())


