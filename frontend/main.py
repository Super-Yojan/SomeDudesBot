import discord
from discord.ext import commands
import asyncio
import os


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/', intents = intents)

from app.commands import remove_roles, add_user_roles, send_challenges,solve_challenges

'''
 All the discord bot commands will be imported here and 
 configured here.
'''

# @bot.command()
@bot.slash_command(guild_ids=[930653648705454120])
async def remove_roles(ctx):
    await remove_roles.remove_all_roles(ctx, bot)

@bot.listen()
async def on_message(message):
    server = bot.get_guild(930653648705454120)
    member = server.get_member(message.author.id)
    await solve_challenges.solve_chall(message,member)

# @bot.command()
@bot.slash_command(guild_ids=[930653648705454120])
async def send_chall(ctx, message):
    if ctx.author.bot == False:
        await send_challenges.send_chall(ctx, message)
    else:
        await ctx.channel.send("A bot can't ask for a challenge!")

token = os.environ['DISCORD_TOKEN']
bot.run(token)
