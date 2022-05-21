'''
Author: Laggstar
'''

import discord, requests
from discord.ext import commands

async def send_chall(ctx, message):
    # print(message)
    if str(message) == "challenge":
        url = "http://backend:8080"
        #{ "id" : 1, "author: : "author", "title" : "title", "challenge" : "Some challenge description"}
        x = requests.get(url)
        challdict = x.json()[-1]
        print(challdict)
        # Get Challenge Name
        embed = discord.Embed(title = challdict["Title"], color=discord.Color.blue())
        # Get Challenge author and description
        embed.add_field(name = challdict["Author"], value = challdict["Description"], inline = False)
        # Footer
        embed.set_footer(text = "Send you answer answer as a file")
        await ctx.message.author.send(embed = embed)
