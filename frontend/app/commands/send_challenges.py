'''
Author: Laggstar
'''

import discord
from discord.ext import commands
from get_challenge import get_chall_from_db

async def send_chall(ctx, message):
    # print(message)
    if str(message) == "challenge":
        #{ "id" : 1, "author: : "author", "title" : "title", "challenge" : "Some challenge description"}
        challdict = get_chall_from_db()
        # Get Challenge Name
        embed = discord.Embed(title = challdict["title"], color=discord.Color.blue())
        # Get Challenge author and description
        embed.add_field(name = challdict["author"], value = challdict["challenge"], inline = False)
        # Footer
        embed.set_footer(text = "Send you answer answer as a file")
        await ctx.message.author.send(embed = embed)