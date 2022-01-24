if message.content.startswith('更改狀態'):
  #切兩刀訊息
  tmp = message.content.split(" ", 2)
  #如果分割後串列長度只有1
  if len(tmp) == 1:
    await message.channel.send("你要改成什麼啦？")

  else:
    game = discord.Game(tmp[1])
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)
