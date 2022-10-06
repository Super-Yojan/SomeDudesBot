'''
Author: Laggstar
'''

import discord


async def add_role(ctx, role, names):
    # Search for role in server
    for name in names:
        if str(role) not in str(ctx.guild.roles):
            await create_Role(ctx, str(role), names)
        else:
            await assign_Role(ctx.author, role)


async def create_Role(ctx, role, names):
    await ctx.guild.create_role(name=role)
    await ctx.send(f'Role `{role}` has been created')
    await assign_Role(ctx.author, role)


async def assign_Role(user, role):
    await user.add_roles(discord.utils.get(user.guild.roles, name=role))
