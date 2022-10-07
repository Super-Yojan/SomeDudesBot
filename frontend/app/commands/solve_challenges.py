"""
drMoscovium

Gets message from the user, and  sends it to the server
"""

import requests
import json
import time
from .add_user_roles import assign_Role


async def solve_chall(message, member):
    print(type(message.author.bot))
    if "Direct Message" in str(message.channel) and message.author.id != "959605476507660298" and not message.author.bot:
        url = "http://backend:8080/solve"
        data = {
            "User": str(message.author),
            "Title": str(message.content),
            "File": (message.attachments[0].url) if len(message.attachments) > 0 else None
        }
        if(data['Title'] == ""):
            newUrl = "http://backend:8080"
            x = requests.get(newUrl)
            challdict = x.json()[-1]
            data['Title'] = challdict['Title'].strip()

        with open("log.txt", 'a') as f:
            f.write(str(message)+"\n")
        x = requests.post(url, json=data)
        rsp = x.json()
        last = rsp['Message'][-20:]
        time = 10
        try:
            time = float(last[last.index('n ')+2:last.index('n ')+7])
        except Exception as e:
            print(e)
            pass
        if "OK" in last:
            if time > 0.08:
                await message.channel.send("Role has been assigned")
                await assign_Role(member, 'SoyDev')
            elif time > 0.05 and time < 0.08:
                await message.channel.send("Role has been assigned")
                await assign_Role(member, 'You are Average In Everything')
            elif time > 0.02 and time < 0.05:
                await message.channel.send("Role has been assigned")
                await assign_Role(member, 'Touch Grass')
            elif time < 0.02:
                await assign_Role(member, '1337ChadC0der')
                await message.channel.send("Role has been assigned")
        else:
            await message.channel.send(rsp['Message'])
            await message.channel.send("If you think you solution is correct and still getting error, check your function signature and make sure to type the title of the challenge. If you are still getting error then contact admin.")
    if message.channel.id == 978889517517901854:
        await message.delete(delay=5.0)
