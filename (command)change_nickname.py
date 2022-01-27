@client.command()
async def changenick(ctx, member: discord.Member, nick):
    target = str(member)

    if target == '紫鹽醬油#9424':
        print(member)
        await ctx.message.author.edit(nick = "笑死 還想搞我啊")

    else:
      await member.edit(nick = nick)
      await ctx.send(f'{member}:已更名為 {member.mention} ')
