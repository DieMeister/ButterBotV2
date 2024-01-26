from datetime import datetime
from colorama import Fore
from id import *
import colors
import data
import log_saves



async def counting(message):
    counting_channel = False
    base = 0
    system = ""
    author = str(message.author.id)
    data.data = data.load_data()
    if message.author.id != bot_id:
        if message.channel.id == channel_normal:
            base = 10
            system = "decimal"
            counting_channel = True
        elif message.channel.id == channel_binär:
            base = 2
            system = "binary"
            counting_channel = True

    if counting_channel:
        if message.author.id != data.data["counting"][system]["last_count"]["member"]:
            message_split = message.content.split(" ")
            number = message_split[0]
            number = int(number, base)

            try:
                if data.data["counting"][system]["last_count"]["number"] == number - 1:
                    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.counting}{system} count set to {colors.variables}{number}")
                    log_saves.save_log(f'{system} count set to "{number}"')

                    data.add_counting(message, author, system)
                    data.add_counting(message, author, "total")

                    data.update_leaderboard(message, author, system)
                    data.update_leaderboard(message, author, "total")

                    data.data["counting"][system]["last_count"]["number"] = number
                    data.data["counting"][system]["last_count"]["member"] = message.author.id

                    data.save_data(data.data)
                else:
                    await message.delete()
                    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{colors.counting}wrong {colors.variables}{system} {colors.counting}number was counted {colors.variables}({bin(number)})")
                    log_saves.save_log(f'wrong "{system}" number was counted ("{bin(number)}")')
            except ValueError:
                await message.delete()
                print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{colors.counting}message didn't start with a {system} number {colors.variables}({message.content})")
                log_saves.save_log(f'''message didn't start with a "{system}" number ("{message.content}")''')
        else:
            await message.delete()
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.counting} same person counted twice in {colors.variables}{message.channel}")
            log_saves.save_log(f'same person counted twice in "{message.channel}"')