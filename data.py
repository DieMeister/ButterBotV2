import json
from colorama import Fore
from datetime import datetime
import colors
import log_saves

data = {}


def add_counting(message, author, system):    
    try:
        data["counting"][system]["individual_count"][author] += 1
    except KeyError:
        data["counting"][system]["individual_count"][author] = 1
    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{message.author.name}{colors.counting}'s {colors.variables}{system} {colors.counting}count was updated to {colors.variables}{data['counting'][system]['individual_count'][author]}")
    log_saves.save_log(f"{message.author.name}'s {system} count was updated to {data['counting'][system]['individual_count'][author]}")


def update_leaderboard(message, author, system):
    leaderboard = data["counting"][system]["leaderboard"]
    if not author in leaderboard:
        leaderboard.append(author)
    if not leaderboard.index(author) == 0:
        position_before = leaderboard.index(author)
        while not leaderboard.index(author) == 0 and data["counting"][system]["individual_count"][author] > data["counting"][system]["individual_count"][leaderboard[leaderboard.index(author) - 1]]:
            index = leaderboard.index(author)
            leaderboard[index] = leaderboard[index - 1]
            leaderboard[index - 1] = author
        if position_before != leaderboard.index(author):
            print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.variables}{message.author.name} {colors.counting}jumped from positon {colors.variables}{position_before + 1} {colors.counting}to position {colors.variables}{leaderboard.index(author) + 1} {colors.counting}on the {colors.variables}total{colors.counting}-leaderboard")
            log_saves.save_log(f"{message.author.name} jumped from positon {position_before + 1} to position {leaderboard.index(author) + 1} on the total-leaderboard")


def load_data():
    with open("data.json") as data_file:
        raw_data = data_file.read()
    data = json.loads(raw_data)
    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.counting}counting stats loaded")
    log_saves.save_log("counting stats loaded")
    return(data)


def save_data(data):
    raw_data = json.dumps(data, indent=4)
    with open("data.json", "w") as data_file:
        data_file.write(raw_data)
    print(f"{Fore.GREEN}{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC:')} {colors.counting}counting stats saved")
    log_saves.save_log("counting stats saved")