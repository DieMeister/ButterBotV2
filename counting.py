from discord.ext import commands
from discord import app_commands
from datetime import datetime
from colors import *
from id import *
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


async def delete_non_decimal_numbers(message):
    if message.channel.id == channel_normal and message.author.id != bot_id:
        if not await check_if_same_author(message):
            numbers = await extract_number_from_message(message)
            message_number = numbers[0]
            old_message_number = numbers[1]
            try:
                if int(old_message_number) == int(message_number) - 1:
                    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_counting}decimal count set to {color_variables}{message_number}")
                    log_saves.save_log(f'decimal count set to "{message_number}"')

                    data.data = data.load_data()
                    data.add_counting(str(message.author.id), "decimal")
                    data.save_data(data.data)
                    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_counting}counting stats saved")
                else:
                    await message.delete()
                    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{color_counting}wrong decimal number was counted {color_variables}({message_number})")
            except ValueError:
                await message.delete()
                print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{color_counting}message didn't start with a decimal number {color_variables}({message.content})")
        else:
            await message.delete()
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_counting} same person counted twice in {color_variables}{message.channel}")


async def delete_non_binary_numbers(message):
    if message.channel.id == channel_binär and message.author.id != bot_id:
        if not await check_if_same_author(message):
            numbers = await extract_number_from_message(message)
            message_number = numbers[0]
            old_message_number = numbers[1]
            try:
                message_number_int = int(message_number, 2)
                old_message_number_int = int(old_message_number, 2)
                if old_message_number_int == message_number_int - 1:
                    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{color_counting}binary count set to {color_variables}{message_number}")
                    log_saves.save_log(f'binary count set to "{message_number}"')

                    data.data = data.load_data()
                    data.add_counting(str(message.author.id), "binary")
                    data.save_data(data.data)
                    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_counting}counting stats saved")
                else:
                    await message.delete()
                    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{color_counting}wrong binary number was counted {color_variables}({message_number})")
            except ValueError:
                await message.delete()
                print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{color_counting}message didn't start with a binary number {color_variables}({message.content})")
        else:
            await message.delete()
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_counting} same person counted twice in {color_variables}{message.channel}")
