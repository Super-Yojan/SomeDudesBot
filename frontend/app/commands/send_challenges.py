'''
Author: Laggstar
'''

import discord
from discord.ext import commands

async def send_chall(ctx, message):
    # print(message)
    if str(message) == "challenge":     
        embed = discord.Embed(title = "Challenge Name", color=discord.Color.blue())
        embed.add_field(name = "Author", value = "Challenge Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Proin libero nunc consequat interdum varius. Viverra justo nec ultrices dui sapien eget. Odio tempor orci dapibus ultrices in. Consequat semper viverra nam libero. Venenatis tellus in metus vulputate eu. At quis risus sed vulputate odio ut. Elementum curabitur vitae nunc sed velit dignissim. Amet nisl suscipit adipiscing bibendum est. Justo laoreet sit amet cursus sit amet dictum sit. Eu tincidunt tortor aliquam nulla facilisi cras fermentum. Etiam non quam lacus suspendisse faucibus interdum posuere lorem. Tincidunt dui ut ornare lectus sit amet est placerat in. Elit pellentesque habitant morbi tristique senectus et netus et. Etiam erat velit scelerisque in dictum non consectetur a.", inline = False)
        embed.set_footer(text = "Send you answer answer as a file")
        await ctx.message.author.send(embed = embed)