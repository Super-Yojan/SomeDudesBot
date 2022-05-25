"""
drMoscovium

Gets message from the user, and  sends it to the server
"""

import requests
import json
from .add_user_roles import assign_Role

async def solve_chall(message,member):
    if "Direct Message" in str(message.channel):
        url = "http://backend:8080/solve"
        data ={
            "User": str(message.author),
            "Title": str(message.content),
            "File": str(message.attachments[0].url)
            }
        x = requests.post(url, json=data)
        rsp =  x.json()
        last = rsp['Message'][-20:]
        if "OK" in last:
            await assign_Role(member,'SoyDev')


