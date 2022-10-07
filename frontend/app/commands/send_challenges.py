'''
Author: Laggstar
'''

import discord
import requests
from discord.ext import commands


async def send_chall(ctx):
    # print(message)
    url = "http://backend:8080"
    # { "id" : 1, "author: : "author", "title" : "title", "challenge" : "Some challenge description"}
    x = requests.get(url)
    challdict = x.json()[-1]
    # Get Challenge Name
    embed = discord.Embed(title=challdict["Title"], color=discord.Color.blue())
    # Get Challenge author and description
    embed.add_field(name=challdict["Author"],
                    value=challdict["Description"], inline=False)
    # Footer
    embed.set_footer(text="Send your answer as a file")
    await ctx.interaction.user.send(embed=embed)
