import discord
from discord.ext import commands
import asyncio
import os


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)

from app.commands import remove_roles, add_roles

'''
 All the discord bot commands will be imported here and 
 configured here.
'''

@bot.command()
async def remove_all_roles(ctx):
    await remove_roles.remove_all_roles(ctx,bot)


@commands.has_permissions(manage_roles=True)
@bot.command()
async def add_roles(ctx):
    await add_roles.add_role(ctx,"Kabir",["Laggstar#4897"])




token = os.environ['DISCORD_TOKEN']
bot.run(token)
