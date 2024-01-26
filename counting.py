from datetime import datetime
from colorama import Fore
from id import *
import colors
import data
import log_saves


async def extract_number_from_message(message):
    message_split = message.content.split(" ")
    message_number = message_split[0]

    message_history = []
    
    async for msg in message.channel.history(limit=2):
        message_history.append(msg.content)
    old_message = message_history[1]
    old_message_slpit = old_message.split(" ")
    old_message_number = old_message_slpit[0]

    return(message_number, old_message_number)


async def check_if_same_author(message):
    author_new_message = message.author
    history = []
    async for msg in message.channel.history(limit=2):
        history.append(msg.author)
    author_old_message = history[1]
    if author_new_message == author_old_message:
        same_person = True
    else:
        same_person = False
    return(same_person)


async def get_last_number(channel):
    history = []
    async for msg in channel.history(limit=1):
        history.append(msg.content)
    message = history[0]
    message_split = message.split(" ")
    count = message_split[0]
    return(count)


async def counting(bot, message):
    counting_channel = False
    base = 0
    system = ""    
    if message.channel.id == channel_normal and message.author.id != bot_id:
        base = 10
        system = "decimal"
        counting_channel = True
    elif message.channel.id == channel_binär and message.author.id != bot_id:
        base = 2
        system = "binary"
        counting_channel = True

    if not await check_if_same_author(message) and counting_channel:
        numbers = await extract_number_from_message(message)
        message_number = numbers[0]
        old_message_number = numbers[1]
        try:
            if int(old_message_number, base) == int(message_number, base) - 1:
                print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.counting}{system} count set to {colors.variables}{message_number}")
                log_saves.save_log(f'{system} count set to "{message_number}"')

                data.data = data.load_data()

                author = str(message.author.id)

                data.add_counting(message, author, system)
                data.add_counting(message, author, "total")

                data.update_leaderboard(message, author, "decimal")
                data.update_leaderboard(message, author, system)

                data.save_data(data.data)
            else:
                await message.delete()
                print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{colors.counting}wrong {system} number was counted {colors.variables}({message_number})")
        except ValueError:
            await message.delete()
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{colors.counting}message didn't start with a {system} number {colors.variables}({message.content})")
    else:
        await message.delete()
        print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.counting} same person counted twice in {colors.variables}{message.channel}")
