
async def add_Role(ctx, role, names): 
    if not role in ctx.guild.roles:
        create_Role(ctx,role)
    else:
        assign_Role(names, role)
        
async def create_Role(ctx, role):
    await ctx.guild.create_role(name=role)

async def assign_Role(ctx, names, role):
    for x in names:
        if not x.has_role(role):
            await x.add_roles(role)
