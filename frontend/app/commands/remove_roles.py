'''
Author: Laggstar
'''

async def remove_all_roles(ctx, bot):
    # Server list 
    serverlist = ["Programmer's Paradise"]
    for guild in bot.guilds:
        if str(guild) in serverlist:
            for member in guild.members:
                # Checks if the user is a bot
                if (member.bot == False):
                    for role in member.roles:
                        try:
                            # Remove all roles
                            await member.remove_roles(role, reason = "Clearing roles", atomic = True)
                        # @everyone/other roles which can't be removed
                        except:
                            print("Role:", role, "not removed for", str(member) + ".")
