@client.event
async def on_message(message):

    bad_words = ["幹", "fuck"]

    if message.author == client.user:
        return

    for word in bad_words:
        if message.content.count(word) > 0:
            print("someone say bad word")
            await message.channel.purge(limit = 1)
            
            #河蟹
            await message.channel.send(":crab:")
