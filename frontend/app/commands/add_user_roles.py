'''
Author: Laggstar
'''
from discord.ext import commands

async def add_role(ctx, role, names):
    # Search for role in server
    for name in names:
        # print("String of role: " + str(role) + ", roles list: " , ctx.guild.roles)
        if str(role) not in str(ctx.guild.roles):
            await create_Role(ctx, str(role), names)
        else:
            await assign_Role(ctx, role, names)

async def create_Role(ctx, role, names):
    await ctx.guild.create_role(name = role)
    await ctx.send(f'Role `{role}` has been created')
    await assign_Role(ctx, role, names)

@commands.has_permissions(administrator=True) 
async def assign_Role(ctx, role, names):
    for name in names:
        for member in ctx.guild.members:
            if name == str(member) and member.bot == False:
                if role not in member.roles:
                    print("Member: " + member)
                    await member.add_roles(role)