if message.content.startswith('抽卡'):
        luck = randrange(1, 10000)
        print(luck)

        # 50% N 1~5000
        if luck < 5001 :
            await message.channel.send("https://imgur.com/7pNp1E0")
            await message.channel.send("普通. (50%)")

        # 30% R 5001~8000
        elif luck < 8001 :
            await message.channel.send("https://imgur.com/PztDT5x")
            await message.channel.send("稀有. (30%)")

        # 15% SR 8001~9500
        elif luck < 9501 :
            await message.channel.send("https://imgur.com/gB7ljt8")
            await message.channel.send("特稀有. (15%)")

        # 4% SSR 9501~9900
        elif luck < 9901 :
            await message.channel.send("https://imgur.com/nyDDgmC")
            await message.channel.send("超級稀有. (4%)")

        # 1% Ultra R 9901~9990
        elif luck < 9991 :
            await message.channel.send("https://imgur.com/MjsJ2cg")
            await message.channel.send("神話. (1%)")

        # 1% legendary 9991~10000
        elif luck < 10001 :
            await message.channel.send("https://c.tenor.com/q4JtK5zE67UAAAAC/power-legendary-reverse-card-econowise-reverse-card.gif")
            await message.channel.send("史詩神話. (0.1%)")

        else:
            await message.channel.send('Error: over estimate.')
