from id import *


async def welcome_message(bot, member,):
    channel = bot.get_channel(channel_preChats_wilkommen)
    await channel.send(f'''
Hallo <@{member.id}>, wilkommen im ButterflyHub.
Um dir selbst Game- oder Länder-Rollen zu geben schau gerne in '**Channels & Roles**'(Kanäle und Rollen) (ganz oben in der Seitenleiste) vorbei.
Wenn du Fragen oder Probleme hast zieh gerne ein Ticket in <#{channel_preChats_staffSupport}>.
Vorschläge, wie der Server (noch) besser werden kann gerne in <#{channel_textChannels_vorschläge}>.
Ansonsten viel Spaß auf dem Server {emoji_butterfly}.
''')