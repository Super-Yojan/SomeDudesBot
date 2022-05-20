import discord
from discord.ext import commands
import asyncio
import os


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/', intents = intents)

from app.commands import remove_roles, add_roles, send_challenges

'''
 All the discord bot commands will be imported here and 
 configured here.
'''

@bot.command()
async def remove_user_roles(ctx):
    await remove_roles.remove_all_roles(ctx, bot)


@commands.has_permissions(manage_roles=True)
@bot.command()
async def add_roles(ctx):
    await add_roles.add_role(ctx,"Kabir",["Laggstar#4897"])

@bot.command()
async def send_challenge(ctx, message):
    if ctx.author.bot == False:
        await send_challenges.send_chall(ctx, message)
    else:
        await ctx.channel.send("A bot can't ask for a challenge!")
    

token = os.environ['DISCORD_TOKEN']
bot.run(token)
