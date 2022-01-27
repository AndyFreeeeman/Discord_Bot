if message.content.startswith('連抽'):
        tmp = message.content.split(" ", 2)

        n_counter = 0
        r_counter = 0
        sr_counter = 0
        ssr_counter = 0
        ur_counter = 0
        l_counter = 0

        if int(tmp[1]) > 10000:
            await message.channel.send("想把我機器搞爆是不是阿")

        else:
            for counter in range(int(tmp[1])):
                luck = randrange(1, 10000)

                if luck < 5001 :
                    n_counter = n_counter + 1
                elif luck < 8001 :
                    r_counter = r_counter + 1
                elif luck < 9501 :
                    sr_counter = sr_counter + 1
                elif luck < 9901 :
                    ssr_counter = ssr_counter + 1
                elif luck < 9991 :
                    ur_counter = ur_counter + 1
                elif luck < 10001 :
                    l_counter = l_counter + 1

            await message.channel.send("共花費 新臺幣 " + str(int(int(tmp[1])/10*80*27.74)) + " 元\n" + tmp[1] + " 抽結果:")
            await message.channel.send("普通卡(50%):      " + str(n_counter) + " 張" + " \n稀有卡(30%):      " + str(r_counter) + " 張" + " \n特稀有卡(15%):    " + str(sr_counter) + " 張" + " \n超級稀有卡(4%):   " + str(ssr_counter) + " 張" + " \n神話卡(1%):            " + str(ur_counter) + " 張" + " \n史詩神話卡(0.1%): " + str(l_counter) + " 張")
