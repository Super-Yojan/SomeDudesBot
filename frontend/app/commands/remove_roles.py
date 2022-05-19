'''
Author: Laggstar
'''

async def remove_all_roles(ctx, bot):
    serverlist = ["Programmer's Paradise"]
    for guild in bot.guilds:
        if str(guild) in serverlist:
            for member in guild.members:
                if (member.bot == False):
                    for role in member.roles:
                        try:
                            await member.remove_roles(role, reason = "Clearing roles", atomic = True)
                        except:
                            print("Role:", role, "not removed for", str(member) + ".")
