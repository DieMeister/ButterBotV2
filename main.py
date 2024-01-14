import discord
from discord import *
from discord.ext import commands
from typing import Literal
from datetime import datetime
from id import *
from colors import *
import counting
import log
import greetings
import log_saves


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents().all())


    async def on_ready(self):
        print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_Bot}Bot is ready")        
        synced = await bot.tree.sync()
        print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_variables}{str(len(synced))} {color_Bot}commands synced")


    async def on_member_join(self, member):
        await greetings.welcome_message(self, member)
        await log.member_join(self, member)

    
    async def on_raw_member_remove(self, payload):
        await log.member_leave(self, payload)


    async def on_message(self, message):
        if not message.content == "":
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_variables}{message.author} {color_messages}sent {color_variables}{message.content} {color_messages}in {color_variables}{message.channel}")
        await counting.delete_non_decimal_numbers(message)
        await counting.delete_non_binary_numbers(message)
        log_saves.save_log(entry=f'"{message.author}" sent "{message.content}" in "{message.channel}"\n')


    async def on_voice_state_update(self, member, before, after):
        await log.voice(self, member, before, after)

    
    async def on_member_update(self, before, after):
        channel = bot.get_channel(channel_log_member)
        if before.nick != after.nick:
            if before.nick == None:
                await channel.send(f'{before.name} added the nickname "{after.nick}" to their server profile')
                print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_variables}{before.name} {color_log}added the nickname {color_variables}{after.nick} {color_log} to their server profile")
                log_saves.save_log(entry=f'"{before.name}" added the nickname "{after.nick}" to their server profile')
            elif after.nick == None:
                await channel.send(f'{before.name} removed the nickname ("{before.nick}") from their server profile')
                print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_variables}{before.name} {color_log}removed the nickname ({color_variables}{before.nick}{color_log}) from their server profile")
                log_saves.save_log(entry=f'"{before.name}" removed the nickname "{before.nick} from their server profile')
            else:
                await channel.send(f"{before.name} changed their nickname from {before.nick} to {after.nick}")
                print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_variables}{before.name} {color_log}changed their nickname from {color_variables}{before.nick} {color_log}to {color_variables}{after.nick}")
                log_saves.save_log(entry=f'"{before.name}" changed their nickname from "{before.nick}" to "{after.nick}')
        if before.roles != after.roles:
            print(before.roles)
            

    async def on_raw_message_edit(self, payload):
        print(RawMessageUpdateEvent.cached_message)


bot = Bot()

@bot.tree.command(name="ping", description="Zeigt den Ping des Bots")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(content=f"Pong - {round(bot.latency*1000)}ms")
    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_commands}command {color_variables}/ping{color_commands} executed")
    log_saves.save_log(entry=f'command "/ping" executed')


@bot.tree.command(name="github", description="Link zum GitHub-Repository")
async def github(interaction: discord.Interaction):
    await interaction.response.send_message(content="[coding (yay)](https://github.com/DieMeister/ButterBot)")
    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_commands}command {color_variables}/github {color_commands}executed")
    log_saves.save_log(entry=f'command "/github" executed')

@bot.tree.command(name="count", description="Zeigt die nächst höhere Zahl an")
async def count(interaction: discord.Interaction):
    channel = bot.get_channel(channel_normal)
    if interaction.channel_id == channel_normal:
        
        count_old = await counting.get_last_number(channel)

        count_new = int(str(count_old)) + 1

        await interaction.response.send_message(content=f"Die nächste Zahl ist {count_new}", ephemeral=True)
        print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_commands}Command {color_variables}/count {color_commands}in {color_variables}{channel} {color_commands}ausgeführt. Die nächste Zahl ist {color_variables}{count_new}")
        log_saves.save_log(entry=f'command "/count" executed in "{channel}". The next number is "{count_new}"')
    elif interaction.channel_id == channel_binär:
        channel = bot.get_channel(channel_binär)

        count_old = await counting.get_last_number(channel)
        count_new_dec = int(count_old, 2) + 1
        count_new_bin = bin(count_new_dec).replace("0b", "")

        await interaction.response.send_message(content=f"Die nächste Zahl ist {count_new_bin} ({count_new_dec})", ephemeral=True)
        print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_commands}Command {color_variables}/count {color_commands}in {color_variables}{channel} {color_commands}ausgeführt. Die nächste Zahl ist {color_variables}{count_new_bin}")
        log_saves.save_log(entry=f'command "/count" executed in "{channel}". The next number is "{count_new_bin}')
    else:
        await interaction.response.send_message(content="Hier kannst du nicht zählen", ephemeral=True)
        print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_commands}Command {color_variables}/count {color_commands}in {color_variables}{channel} {color_commands}ausgeführt. Hier kann man nicht zählen")
        log_saves.save_log(entry=f'command "/count" executed in "{channel}". This is not a counting channel')


@bot.tree.command(name="leaderboard", description="Zeigt die Bestenliste der counting-channel")
async def leaderboard(interaction: discord.Interaction, type: Literal["total", "dezimal", "binär"]):
    if interaction.channel.id == channel_binär or channel_normal:
        if type == "total":
            embed = discord.Embed(title="Bestenliste", color=discord.Color.orange(), timestamp=datetime.utcnow())
            embed.add_field(name="Gesamt", value="test")
            await interaction.response.send_message(content="test", ephemeral=True)
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {color_commands}command {color_variables}leaderboard {color_commands}executed")

bot.run(bot_token)
