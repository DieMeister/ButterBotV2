from datetime import datetime
from colorama import Fore
from id import *
import log_saves
import colors


async def voice(bot, member, before, after ):
    channel = bot.get_channel(channel_log_voice)
    if before.channel != after.channel:
        if before.channel == None:
            await channel.send(f"<@{member.id}> joined <#{after.channel.id}>")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}joined {colors.variables}{after.channel.name}")
            log_saves.save_log(entry=f'"{member.name}" joined "{after.channel.name}"')
        elif after.channel == None:
            await channel.send(f"<@{member.id}> left <#{before.channel.id}>")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}left {colors.variables}{before.channel.name}")
            log_saves.save_log(entry=f'"{member.name}" left "{before.channel.name}"')
        else:
            await channel.send(f"<@{member.id}> switched VoiceChannel from <#{before.channel.id}> to <#{after.channel.id}>")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}switched voice channel from {colors.variables}{before.channel.name} {colors.log}to {colors.variables}{after.channel.name}")
            log_saves.save_log(f'"{member.name}" switched voice channel from "{before.channel.name}" to "{after.channel.name}"')
    if before.mute != after.mute:
        if after.mute:
            await channel.send(f"<@{member.id}> was muted by a team member")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}was muted by a team member")
            log_saves.save_log(f'"{member.name}" was muted by a team member')
        if not after.mute:
            await channel.send(f"<@{member.id}> was unmuted by a team member")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}was unmuted by a team member")
            log_saves.save_log(f'"{member.name}" was unmuted by a team member')
    if before.deaf != after.deaf:
        if after.deaf:
            await channel.send(f"<@{member.id}> was deafened by a team member")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}was deafened by a team member")
            log_saves.save_log(f'"{member.name}" was deafened by a team member')
        if not after.deaf:
            await channel.send(f"<@{member.id}> was undeafened by a team member")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}was undeafened by a team member")
            log_saves.save_log(f'"{member.name}" was undeafened by a team member')
    if before.self_mute != after.self_mute:
        if after.self_mute:
            await channel.send(f"<@{member.id}> muted themself")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}muted themself")
            log_saves.save_log(f'"{member.name}" muted themself')
        if not after.self_mute:
            await channel.send(f"<@{member.id}> unmuted themself")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}unmuted themself")
            log_saves.save_log(f'"{member.name}" unmuted themself')
    if before.self_deaf != after.self_deaf:
        if after.self_deaf:
            await channel.send(f"<@{member.id}> deafened themself")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}deafened themself")
            log_saves.save_log(f'"{member.name}" deafened themself')
        if not after.self_deaf:
            await channel.send(f"<@{member.id}> undeafened themself")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}undeafened themself")
            log_saves.save_log(f'"{member.name}" unmuted themself')
    if before.self_video != after.self_video:
        if after.self_video:
            await channel.send(f"<@{member.id}> turned on their camera")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}turned on their camera")
            log_saves.save_log(f'"{member.name}" turned on their camera')
        if not after.self_video:
            await channel.send(f"<@{member.id}> turned off their camera")
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{member.name} {colors.log}turned off their camera")
            log_saves.save_log(f'"{member.name}" turned off their camera')


async def member_join(bot, member):
    channel = bot.get_channel(channel_log_member)
    await channel.send(f"<@{member.id}> joined the server")
    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{colors.variables}{member.name} {colors.log}joined the server")
    log_saves.save_log(f'"{member.id}" joined the server')

async def member_leave(bot, payload):
    channel = bot.get_channel(channel_log_member)
    member = payload.user
    await channel.send(f"<@{member.id}> left the server")
    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC: ')}{colors.variables}{member.name} {colors.log}left the server")
    log_saves.save_log(f'"{member.id}" left the server')
