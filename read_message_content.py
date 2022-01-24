@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('整天看這些'):
        await message.channel.send('我就喜歡看')

    if message.content.startswith('伺服器狀況'):
        await message.channel.send(
            'https://minecraft-mp.com/banner-81821-5.png')

    if '遊戲' in message.content:
        await message.channel.send('還在玩遊戲')
